package ossproj.demo.util;

import io.jsonwebtoken.*;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;
import ossproj.demo.dto.JwtToken;

import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.util.Arrays;
import java.util.Base64;
import java.util.Collection;
import java.util.Date;
import java.util.stream.Collectors;

@Slf4j
@Component
public class JwtTokenProvider {

    private final Key key;

    // application.yml에서 secret 값을 가져오고 key 저장
    public JwtTokenProvider(@Value("${DB_SECRET}") String secretKey) {
        System.out.println("secretKey = " + secretKey);
        byte[] keyBytes = hexStringToByteArray(secretKey);
        this.key = Keys.hmacShaKeyFor(keyBytes);
        System.out.println("Key bytes: " + Arrays.toString(keyBytes));
    }

    /**
     * 인증(Authentication) 객체를 기반으로 Access Token과 Refresh Token 생성
     * Access Token: 인증된 사용자의 권한 정보와 만료 시간을 담고 있음
     * Refresh Token: Access Token의 갱신을 위해 사용 됨
     * @param authentication
     * @return
     */
    public JwtToken generateToken(Authentication authentication) {
        String authorities = authentication.getAuthorities().stream()
                .map(GrantedAuthority::getAuthority)
                .collect(Collectors.joining(","));

        long now = (new Date()).getTime();

        Date accessTokenExpiresIn = new Date(now + 86400000);
        String accessToken = Jwts.builder()
                .setSubject(authentication.getName())
                .claim("auth", authorities)
                .setExpiration(accessTokenExpiresIn)
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();

        // Refresh Token 생성
        String refreshToken = Jwts.builder()
                .setExpiration(new Date(now + 86400000))
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();

        return JwtToken.builder()
                .grantType("Bearer")
                .accessToken(accessToken)
                .refreshToken(refreshToken)
                .build();
    }

    /**
     * 주어진 Access token을 복호화하여 사용자의 인증 정보(Authentication)를 생성
     * 토큰의 Claims에서 권한 정보를 추출하고, User 객체를 생성하여 Authentication 객체로 반환
     *
     * 토큰의 클레임에서 권한 정보를 가져옴. "auth" 클레임은 토큰에 저장된 권한 정보를 나타냄
     * 가져온 권한 정보를 SimpleGrantedAuthority 객체로 변환하여 컬렉션에 추가
     * UserDetails 객체를 생성하여 주체(subject)와 권한 정보, 기타 필요한 정보를 설정
     * UsernamepasswordAuthenticationToken 객체를 생성하여 주체와 권한 정보를 포함한 인증(Authentication) 객체를 생성
     * @param accessToken
     * @return
     */
    public Authentication getAuthentication(String accessToken) {
        Claims claims = parseClaims(accessToken);

        if (claims.get("auth") == null) {
            throw new RuntimeException("권한 정보가 없는 토큰입니다.");
        }
        // 클레임에서 권한 정보 가져오기
        Collection<? extends GrantedAuthority> authorities =
                Arrays.stream(claims.get("auth").toString().split(","))
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());

        // UserDetails 객체를 만들어서 Authentication return
        // UserDetails: interface, User: UserDetails를 구현한 class
        UserDetails principal = new User(claims.getSubject(), "", authorities);
        return new UsernamePasswordAuthenticationToken(principal, "", authorities);
    }


    // 토큰 정보를 검증하는 메서드

    /**
     * 주어진 토큰을 검증하여 유효성을 확인
     * Jwts.parserBuilder를 사용하여 토큰의 서명 키를 설정하고, 예외 처리를 통해 토큰의 유효성 여부를 판단
     * 🧐 IllegalArgumentException 발생하는 경우
     * ➡️ 토큰이 올바른 형식이 아니거나 클레임이 비어있는 경우 등에 발생
     * claim.getSubject()는 주어진 토큰의 클레임에서 "sub" 클레임의 값을 반환
     * ➡️ 토큰의 주체를 나타냄. ex) 사용자의 식별자나 이메일 주소
     * @param token
     * @return
     */
    public boolean validateToken(String token) {
        try {
            System.out.println("token = " + token);
            Jwts.parserBuilder()
                    .setSigningKey(key)
                    .build()
                    .parseClaimsJws(token);
            return true;
        } catch (SecurityException | MalformedJwtException e) {
            log.info("Invalid JWT Token", e);
        } catch (ExpiredJwtException e) {
            log.info("Expired JWT Token", e);
        } catch (UnsupportedJwtException e) {
            log.info("Unsupported JWT Token", e);
        } catch (IllegalArgumentException e) {
            log.info("JWT claims string is empty.", e);
        }
        return false;
    }

    /**
     * 클레임(Claims): 토큰에서 사용할 정보의 조각
     * 주어진 Access token을 복호화하고, 만료된 토큰인 경우에도 Claims 반환
     * parseClaimsJws() 메서드가 JWT 토큰의 검증과 파싱을 모두 수행
     * @param accessToken
     * @return
     */
    private Claims parseClaims(String accessToken) {
        try {
            return Jwts.parserBuilder()
                    .setSigningKey(key)
                    .build()
                    .parseClaimsJws(accessToken)
                    .getBody();
        } catch (ExpiredJwtException e) {
            return e.getClaims();
        }
    }
    public static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4)
                    + Character.digit(s.charAt(i + 1), 16));
        }
        return data;
    }
}
