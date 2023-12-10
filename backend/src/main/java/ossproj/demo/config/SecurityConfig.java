package ossproj.demo.config;

import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.factory.PasswordEncoderFactories;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import ossproj.demo.util.JwtTokenProvider;

import java.util.Arrays;
import java.util.Collections;

@Configuration
@EnableWebSecurity
@RequiredArgsConstructor
public class SecurityConfig {

    private final JwtTokenProvider jwtTokenProvider;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
        return httpSecurity
                .cors(corsCustomizer -> corsCustomizer.configurationSource(request -> {
                    CorsConfiguration config = new CorsConfiguration();
                    config.setAllowedOriginPatterns(Collections.singletonList("*")); // 모든 오리진 허용
                    config.setAllowCredentials(true); // 크로스 오리진 요청에서 사용자 인증 정보 허용
                    config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE", "OPTIONS")); // 모든 HTTP 메소드 허용
                    config.setAllowedHeaders(Arrays.asList("Authorization", "Cache-Control", "Content-Type")); // 필요한 헤더 허용
                    config.setMaxAge(3600L); // 1시간
                    return config;
                }))
                // HTTP Basic 인증 비활성화
                .httpBasic(httpBasicConfigurer -> httpBasicConfigurer.disable())
                // CSRF 보안 비활성화
                .csrf(csrf -> csrf.disable())
                // 세션 관리 비활성화
                .sessionManagement(sessionManagement -> sessionManagement.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                // 권한 요청 처리
                .authorizeRequests(authorize -> authorize
                        .requestMatchers("/users/**").permitAll() // 공개 경로
                        .requestMatchers(HttpMethod.POST, "/users/**").hasRole("USER") // USER 역할이 필요한 경로, GET 요청에 대해서만
                        .anyRequest().authenticated() // 그 외의 모든 요청은 인증 필요
                )

                // JWT 인증 필터 추가
                .addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider), UsernamePasswordAuthenticationFilter.class)
                .build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        // BCrypt Encoder 사용
        return PasswordEncoderFactories.createDelegatingPasswordEncoder();
    }


}