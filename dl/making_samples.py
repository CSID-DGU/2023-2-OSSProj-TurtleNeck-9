from study_system import study_system

ISE=study_system()
ISE.name2id={"산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","인간공학":"ISE2004","데이터분석입문":"ISE2021","3D모델링":"ISE2025","산업시스템프로그래밍1":"ISE2024","어드벤처디자인":"ISE2022","경영과학1":"ISE2016","산업시스템공학의이해":"ISE2018","응용통계학":"ISE2017","정보시스템분석설계":"ISE2023","생산및운영관리":"ISE4002","첨단제조공학":"ISE4005","금융공학입문":"ISE4008","프로젝트관리":"ISE4011","경영과학2":"ISE4014","유통물류관리":"ISE4018","UI/UX설계":"ISE4044","시뮬레이션과응용":"ISE4021","제품개발":"ISE4022","기술경영":"ISE4023","산업시스템공학종합설계":"ISE4026","산업시스템프로그래밍2":"ISE4047","서비스공학":"ISE4029","정보시스템통합및실습":"ISE4032","머신러닝1":"ISE4045","머신러닝2":"ISE4046","헬스케어공학":"ISE4036","실험계획법":"ISE4037","품질공학":"ISE4038","데이터어낼리틱스":"ISE4041","산업AI":"ISE4042","기술창업캡스톤디자인2":"DES4032","기업사회맞춤형캡스톤디자인2":"DES4025","다학제캡스톤디자인":"DES4009"}#캡스톤디자인대회는 비교과과정이라 id가 없어 이렇게 설정했음
ISE.grade2names={11:["산업시스템공학의이해"],12:["어드벤처디자인"],
                 21:["응용통계학","인간공학","3D모델링","산업시스템프로그래밍1"],
                 22:["경영과학1","데이터분석입문","정보시스템분석설계","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)"],
                 31:["금융공학입문","경영과학2","머신러닝1","실험계획법","생산및운영관리"],
                 32:["품질공학","첨단제조공학","머신러닝2","기술경영","유통물류관리","헬스케어공학","산업시스템프로그래밍2"],
                 41:["서비스공학","프로젝트관리","시뮬레이션과응용","데이터어낼리틱스","정보시스템통합및실습","산업시스템공학종합설계"],
                 42:["제품개발","UI/UX설계","산업AI","기업사회맞춤형캡스톤디자인2","기술창업캡스톤디자인2","다학제캡스톤디자인"]}
ISE.insert_last(subj_name="산업시스템공학의이해",grade=11)
ISE.insert_last(subj_name="어드벤처디자인",grade=12,prev_subj_rec_names=["산업시스템공학의이해"])
ISE.insert_last(subj_name="응용통계학",grade=21);ISE.insert_last(subj_name="3D모델링",grade=21);ISE.insert_last(subj_name="인간공학",grade=21);ISE.insert_last(subj_name="산업시스템프로그래밍1",grade=21)
ISE.insert_last(subj_name="경영과학1",grade=22);ISE.insert_last("데이터분석입문",grade=22,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="정보시스템분석설계",grade=22);ISE.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22)
ISE.insert_last(subj_name="경영과학2",grade=31,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="실험계획법",grade=31,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="머신러닝1",grade=31,prev_subj_rec_names=["데이터분석입문"]);ISE.insert_last(subj_name="생산및운영관리",grade=31);ISE.insert_last(subj_name="금융공학입문",grade=31,prev_subj_nec_names=["응용통계학"])
ISE.insert_last(subj_name="품질공학",grade=32,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="첨단제조공학",grade=32);ISE.insert_last(subj_name="머신러닝2",grade=32,prev_subj_rec_names=["머신러닝1"]);ISE.insert_last(subj_name="기술경영",grade=32,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="유통물류관리",grade=32,prev_subj_nec_names=["생산및운영관리","경영과학1"]);ISE.insert_last(subj_name="헬스케어공학",grade=32,prev_subj_rec_names=["인간공학"]);ISE.insert_last(subj_name="산업시스템프로그래밍2",grade=32,prev_subj_rec_names=["산업시스템프로그래밍1"])
ISE.insert_last(subj_name="서비스공학",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="프로젝트관리",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="시뮬레이션과응용",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="데이터어낼리틱스",grade=41,prev_subj_rec_names=["머신러닝1","머신러닝2"]);ISE.insert_last(subj_name="정보시스템통합및실습",grade=41,prev_subj_rec_names=["정보시스템분석설계"]);ISE.insert_last(subj_name="산업시스템공학종합설계",grade=41,prev_subj_nec_names=["산업시스템공학의이해","어드벤처디자인","응용통계학","산업시스템프로그래밍1","경영과학1"])
ISE.insert_last(subj_name="제품개발",grade=42);ISE.insert_last(subj_name="UI/UX설계",grade=42,prev_subj_rec_names=["인간공학","정보시스템분석설계"]);ISE.insert_last(subj_name="산업AI",grade=42,prev_subj_rec_names=["정보시스템분석설계"]);ISE.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42);ISE.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);ISE.insert_last(subj_name="다학제캡스톤디자인",grade=42);
samplesISE1=ISE.random_sampling(400,n1=1,n2=1,n3=3,n4=3,n5=3,n6=5,n7=5,n8=2)
samplesISE2=ISE.random_sampling(400,n1=1,n2=1,n3=4,n4=2,n5=4,n6=5,n7=4,n8=3)
samplesISE3=ISE.random_sampling(400,n1=1,n2=1,n3=3,n4=2,n5=5,n6=6,n7=5,n8=3)
samplesISE4=ISE.random_sampling(400,n1=1,n2=1,n3=4,n4=3,n5=4,n6=4,n7=4,n8=4)
samplesISE5=ISE.random_sampling(400,n1=1,n2=1,n3=3,n4=4,n5=3,n6=4,n7=6,n8=2)
samplesISE6=ISE.random_sampling(400,n1=1,n2=1,n3=2,n4=4,n5=4,n6=5,n7=3,n8=3)
AllsamplesISE=[]
ISElist=[samplesISE1,samplesISE2,samplesISE3,samplesISE4,samplesISE5,samplesISE6]
for isedataset in ISElist:
    AllsamplesISE.extend(isedataset)
print("전체 산시 샘플 수 : ",len(AllsamplesISE))

EE=study_system()
EE.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],21:["전기회로실험","C언어및자료구조","디지털공학","전자기학1","물리전자공학1","회로이론1"],
                22:["산학융합종합설계","디지털실험","객체지향프로그래밍","신호및시스템","논리회로설계","전자기학2","물리전자공학2","회로이론2"],
                 31:["초고주파공학","랜덤신호이론","통신이론","디지털신호처리및설계","마이크로프로세서응용및실험","컴퓨터구조및설계","고체전자소자","전자회로1","전기기계1","전력공학1","전기전자재료공학"],
                 32:["안테나공학","디지털통신","기계학습론","영상처리","제어공학개론","센서응용공학","SoC설계","반도체공정","전자회로실험","전자회로2","전기기계2","전력공학2","고전압공학"],
                 41:["캡스톤디자인","IoT통신및실습","영상및딥러닝프로그래밍","현대제어공학","로봇공학","디지털집적회로설계","광전자공학","전력전자공학","전력시스템응용","전자에너지변환공학","전기설비공학개론"],
                 42:["임베디드신호처리시스템","아날로그집적회로","나노전자기계공학","신재생에너지","전동력제어및응용","분산전원시스템","전기응용","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE1=study_system()
EE1.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE1.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],
                 21:["전기회로실험","C언어및자료구조","디지털공학","회로이론1"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","디지털실험","객체지향프로그래밍","신호및시스템","논리회로설계","회로이론2"],
                 31:["랜덤신호이론","통신이론","디지털신호처리및설계","전자회로1"],
                 32:["기계학습론","영상처리","전자회로실험","전자회로2"],
                 41:["캡스톤디자인","영상및딥러닝프로그래밍"],
                 42:["분산전원시스템","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE1.insert_last(subj_name="어드벤처디자인",grade=11);EE1.insert_last(subj_name="어드벤처디자인",grade=12);EE1.insert_last(subj_name="공학프로그램응용",grade=12)
EE1.insert_last(subj_name="회로이론1",grade=21);EE1.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE1.insert_last(subj_name="디지털공학",grade=21);EE1.insert_last(subj_name="C언어및자료구조",grade=21,prev_subj_rec_names=["공학프로그램응용"])
EE1.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE1.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE1.insert_last(subj_name="디지털실험",grade=22,prev_subj_rec_names=["디지털공학"]);EE1.insert_last(subj_name="논리회로설계",grade=22,prev_subj_nec_names=["디지털공학"]);EE1.insert_last(subj_name="객체지향프로그래밍",grade=22,prev_subj_rec_names=["C언어및자료구조"]);EE1.insert_last(subj_name="신호및시스템",grade=22,prev_subj_rec_names=["공학프로그램응용"])
EE1.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE1.insert_last(subj_name="랜덤신호이론",grade=31);EE1.insert_last(subj_name="디지털신호처리및설계",grade=31,prev_subj_nec_names=["신호및시스템"]);EE1.insert_last(subj_name="통신이론",grade=31)
EE1.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE1.insert_last(subj_name="전자회로실험",grade=32,prev_subj_rec_names=["전자회로1"]);EE1.insert_last(subj_name="기계학습론",grade=32,prev_subj_rec_names=["객체지향프로그래밍"]);EE1.insert_last(subj_name="영상처리",grade=32,prev_subj_rec_names=["객체지향프로그래밍","디지털신호처리및설계"])
EE1.insert_last(subj_name="영상및딥러닝프로그래밍",grade=41,prev_subj_rec_names=["기계학습론","영상처리"]);EE1.insert_last(subj_name="캡스톤디자인",grade=41)
EE1.insert_last(subj_name="분산전원시스템",grade=42);EE1.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE1.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE1.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE1_1=EE1.random_sampling(100,n1=1,n2=1,n3=3,n4=3,n5=2,n6=3,n7=2,n8=1)
samplesEE1_2=EE1.random_sampling(100,n1=1,n2=1,n3=4,n4=4,n5=1,n6=2,n7=1,n8=2)
samplesEE1_3=EE1.random_sampling(100,n1=1,n2=1,n3=3,n4=5,n5=3,n6=2,n7=2,n8=1)

EE2=study_system()
EE2.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE2.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],
                 21:["전기회로실험","C언어및자료구조","디지털공학","전자기학1","물리전자공학1","회로이론1"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","디지털실험","신호및시스템","전자기학2","물리전자공학2","회로이론2"],
                 31:["초고주파공학","랜덤신호이론","통신이론","디지털신호처리및설계","전자회로1"],
                 32:["안테나공학","디지털통신","전자회로2","고전압공학"],
                 41:["캡스톤디자인","IoT통신및실습","광전자공학"],
                 42:["다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE2.insert_last(subj_name="어드벤처디자인",grade=11);EE2.insert_last(subj_name="어드벤처디자인",grade=12);EE2.insert_last(subj_name="공학프로그램응용",grade=12)
EE2.insert_last(subj_name="회로이론1",grade=21);EE2.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE2.insert_last(subj_name="전자기학1",grade=21);EE2.insert_last(subj_name="C언어및자료구조",grade=21,prev_subj_rec_names=["공학프로그램응용"]);EE2.insert_last(subj_name="디지털공학",grade=21);EE2.insert_last(subj_name="물리전자공학1",grade=21)
EE2.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE2.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE2.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["전자기학1"]);EE2.insert_last(subj_name="신호및시스템",grade=22,prev_subj_rec_names=["C언어및자료구조"]);EE2.insert_last(subj_name="물리전자공학2",grade=22,prev_subj_nec_names=["물리전자공학1"]);EE2.insert_last(subj_name="디지털실험",grade=22,prev_subj_rec_names=["디지털공학"])
EE2.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE2.insert_last(subj_name="초고주파공학",grade=31,prev_subj_rec_names=["전자기학2"]);EE2.insert_last(subj_name="통신이론",grade=31,prev_subj_nec_names=["신호및시스템"]);EE2.insert_last(subj_name="랜덤신호이론",grade=31,prev_subj_rec_names=["신호및시스템","통신이론"]);EE2.insert_last(subj_name="디지털신호처리및설계",grade=31)
EE2.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE2.insert_last(subj_name="안테나공학",grade=32,prev_subj_rec_names=["초고주파공학"]);EE2.insert_last(subj_name="디지털통신",grade=32,prev_subj_rec_names=["랜덤신호이론","통신이론"]);EE2.insert_last(subj_name="고전압공학",grade=32)
EE2.insert_last(subj_name="캡스톤디자인",grade=41);EE2.insert_last(subj_name="IoT통신및실습",grade=41,prev_subj_rec_names=["안테나공학","디지털통신"]);EE2.insert_last(subj_name="광전자공학",grade=41)
EE2.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE2.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE2.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE2_1=EE2.random_sampling(100,n1=1,n2=1,n3=5,n4=4,n5=4,n6=4,n7=2,n8=1)
samplesEE2_2=EE2.random_sampling(100,n1=1,n2=1,n3=4,n4=3,n5=5,n6=2,n7=3,n8=1)
samplesEE2_3=EE2.random_sampling(100,n1=1,n2=1,n3=6,n4=5,n5=3,n6=3,n7=2,n8=1)

EE3=study_system()
EE3.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE3.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],
                 21:["전기회로실험","C언어및자료구조","디지털공학","전자기학1","회로이론1"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","디지털실험","신호및시스템","논리회로설계","전자기학2","회로이론2"],
                 31:["디지털신호처리및설계","마이크로프로세서응용및실험","컴퓨터구조및설계","고체전자소자","전자회로1","전기전자재료공학"],
                 32:["제어공학개론","센서응용공학","SoC설계","전자회로실험","전자회로2"],
                 41:["캡스톤디자인","현대제어공학","로봇공학","광전자공학","전력전자공학",],
                 42:["임베디드신호처리시스템","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE3.insert_last(subj_name="어드벤처디자인",grade=11);EE3.insert_last(subj_name="어드벤처디자인",grade=12);EE3.insert_last(subj_name="공학프로그램응용",grade=12)
EE3.insert_last(subj_name="회로이론1",grade=21);EE3.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE3.insert_last(subj_name="디지털공학",grade=21);EE3.insert_last(subj_name="C언어및자료구조",grade=21);EE3.insert_last(subj_name="전자기학1",grade=21)
EE3.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE3.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE3.insert_last(subj_name="디지털실험",grade=22,prev_subj_rec_names=["디지털공학"]);EE3.insert_last(subj_name="논리회로설계",grade=22,prev_subj_rec_names=["디지털공학"]);EE3.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["전자기학1"]);EE3.insert_last(subj_name="신호및시스템",grade=22)
EE3.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE3.insert_last(subj_name="컴퓨터구조및설계",grade=31,prev_subj_rec_names=["논리회로설계"]);EE3.insert_last(subj_name="마이크로프로세서응용및실험",grade=31,prev_subj_rec_names=["회로이론2"]);EE3.insert_last(subj_name="디지털신호처리및설계",grade=31);EE3.insert_last(subj_name="고체전자소자",grade=31);EE3.insert_last(subj_name="전기전자재료공학",grade=31)
EE3.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE3.insert_last(subj_name="SoC설계",grade=32,prev_subj_rec_names=["컴퓨터구조및설계"]);EE3.insert_last(subj_name="제어공학개론",grade=32);EE3.insert_last(subj_name="센서응용공학",grade=32);EE3.insert_last(subj_name="전자회로실험",grade=32,prev_subj_rec_names=["전자회로1"])
EE3.insert_last(subj_name="캡스톤디자인",grade=41);EE3.insert_last(subj_name="현대제어공학",grade=41,prev_subj_rec_names=["제어공학개론","센서응용공학"]);EE3.insert_last(subj_name="로봇공학",grade=41,prev_subj_rec_names=["제어공학개론","센서응용공학"]);EE3.insert_last(subj_name="광전자공학",grade=41);EE3.insert_last(subj_name="전력전자공학",grade=41)
EE3.insert_last(subj_name="임베디드신호처리시스템",grade=42);EE3.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE3.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE3.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE3_1=EE3.random_sampling(100,n1=1,n2=1,n3=4,n4=4,n5=4,n6=4,n7=4,n8=1)
samplesEE3_2=EE3.random_sampling(100,n1=0,n2=2,n3=5,n4=4,n5=6,n6=3,n7=3,n8=2)
samplesEE3_3=EE3.random_sampling(100,n1=0,n2=2,n3=4,n4=5,n5=5,n6=3,n7=4,n8=1)


EE4=study_system()
EE4.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE4.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],
                 21:["전기회로실험","C언어및자료구조","디지털공학","전자기학1","물리전자공학1","회로이론1"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","객체지향프로그래밍","신호및시스템","논리회로설계","전자기학2","물리전자공학2","회로이론2"],
                 31:["랜덤신호이론","통신이론","디지털신호처리및설계","마이크로프로세서응용및실험","전자회로1"],
                 32:["기계학습론","영상처리","제어공학개론","SoC설계","전자회로2"],
                 41:["캡스톤디자인","영상및딥러닝프로그래밍","로봇공학"],
                 42:["임베디드신호처리시스템","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE4.insert_last(subj_name="어드벤처디자인",grade=11);EE4.insert_last(subj_name="어드벤처디자인",grade=12);EE4.insert_last(subj_name="공학프로그램응용",grade=12)
EE4.insert_last(subj_name="회로이론1",grade=21);EE4.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE4.insert_last(subj_name="전자기학1",grade=21);EE4.insert_last(subj_name="C언어및자료구조",grade=21,prev_subj_rec_names=["공학프로그램응용"]);EE4.insert_last(subj_name="디지털공학",grade=21);EE4.insert_last(subj_name="물리전자공학1",grade=21)
EE4.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE4.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE4.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["전자기학1"]);EE4.insert_last(subj_name="신호및시스템",grade=22,prev_subj_rec_names=["공학프로그램응용"]);EE4.insert_last(subj_name="객체지향프로그래밍",grade=22,prev_subj_rec_names=["C언어및자료구조"]);EE4.insert_last(subj_name="논리회로설계",grade=22,prev_subj_nec_names=["디지털공학"]);EE4.insert_last(subj_name="물리전자공학2",grade=22,prev_subj_nec_names=["물리전자공학1"])
EE4.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE4.insert_last(subj_name="디지털신호처리및설계",grade=31,prev_subj_nec_names=["신호및시스템"]);EE4.insert_last(subj_name="마이크로프로세서응용및실험",grade=31,prev_subj_rec_names=["C언어및자료구조"]);EE4.insert_last(subj_name="랜덤신호이론",grade=31);EE4.insert_last(subj_name="통신이론",grade=31)
EE4.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE4.insert_last(subj_name="기계학습론",grade=32,prev_subj_rec_names=["디지털신호처리및설계"]);EE4.insert_last(subj_name="영상처리",grade=32,prev_subj_rec_names=["객체지향프로그래밍","기계학습론"]);EE4.insert_last(subj_name="SoC설계",grade=32);EE4.insert_last(subj_name="제어공학개론",grade=32)
EE4.insert_last(subj_name="캡스톤디자인",grade=41);EE4.insert_last(subj_name="영상및딥러닝프로그래밍",grade=41,prev_subj_rec_names=["기계학습론","영상처리"]);EE4.insert_last(subj_name="로봇공학",grade=41)
EE4.insert_last(subj_name="임베디드신호처리시스템",grade=42,prev_subj_rec_names=["기계학습론","마이크로프로세서응용및실험"]);EE4.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE4.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE4.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE4_1=EE4.random_sampling(100,n1=1,n2=1,n3=5,n4=4,n5=4,n6=3,n7=2,n8=1)
samplesEE4_2=EE4.random_sampling(100,n1=0,n2=2,n3=4,n4=5,n5=4,n6=4,n7=2,n8=2)
samplesEE4_3=EE4.random_sampling(100,n1=0,n2=2,n3=6,n4=5,n5=3,n6=4,n7=3,n8=1)

EE5=study_system()
EE5.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE5.grade2names={11:["어드벤처디자인"],12:["어드벤처디자인"],
                 21:["전기회로실험","디지털공학","전자기학1","물리전자공학1","회로이론1","C언어및자료구조"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","디지털실험","논리회로설계","전자기학2","물리전자공학2","회로이론2"],
                 31:["마이크로프로세서응용및실험","고체전자소자","전자회로1"],
                 32:["반도체공정","전자회로실험","전자회로2"],
                 41:["캡스톤디자인","디지털집적회로설계","광전자공학"],
                 42:["아날로그집적회로","나노전자기계공학","전기응용","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE5.insert_last(subj_name="어드벤처디자인",grade=11);
EE5.insert_last(subj_name="어드벤처디자인",grade=12);
EE5.insert_last(subj_name="회로이론1",grade=21);EE5.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE5.insert_last(subj_name="디지털공학",grade=21);EE5.insert_last(subj_name="물리전자공학1",grade=21);EE5.insert_last(subj_name="전자기학1",grade=21);EE5.insert_last(subj_name="C언어및자료구조",grade=21)
EE5.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE5.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE5.insert_last(subj_name="디지털실험",grade=22,prev_subj_rec_names=["디지털공학"]);EE5.insert_last(subj_name="논리회로설계",grade=22,prev_subj_nec_names=["디지털공학"]);EE5.insert_last(subj_name="물리전자공학2",grade=22,prev_subj_nec_names=["물리전자공학1"]);EE5.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["전자기학1"])
EE5.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE5.insert_last(subj_name="고체전자소자",grade=31,prev_subj_rec_names=["물리전자공학2"]);EE5.insert_last(subj_name="마이크로프로세서응용및실험",grade=31,prev_subj_rec_names=["C언어및자료구조"])
EE5.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE5.insert_last(subj_name="전자회로실험",grade=32,prev_subj_rec_names=["전자회로1"]);EE5.insert_last(subj_name="반도체공정",grade=32,prev_subj_rec_names=["고체전자소자","전자기학2"])
EE5.insert_last(subj_name="캡스톤디자인",grade=41);EE5.insert_last(subj_name="디지털집적회로설계",grade=41,prev_subj_nec_names=["논리회로설계"]);EE5.insert_last(subj_name="광전자공학",grade=41,prev_subj_nec_names=["고체전자소자"])
EE5.insert_last(subj_name="아날로그집적회로",grade=42);EE5.insert_last(subj_name="나노전자기계공학",grade=42,prev_subj_rec_names=["고체전자소자"]);EE5.insert_last(subj_name="전기응용",grade=42);EE5.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE5.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE5.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE5_1=EE5.random_sampling(75,n1=1,n2=1,n3=5,n4=4,n5=3,n6=3,n7=3,n8=2)
samplesEE5_2=EE5.random_sampling(75,n1=1,n2=0,n3=6,n4=5,n5=2,n6=3,n7=2,n8=3)
samplesEE5_3=EE5.random_sampling(75,n1=1,n2=1,n3=4,n4=5,n5=3,n6=2,n7=3,n8=3)
samplesEE5_4=EE5.random_sampling(75,n1=1,n2=0,n3=5,n4=4,n5=3,n6=3,n7=2,n8=2)



EE6=study_system()
EE6.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE6.grade2names={11:["어드벤처디자인"],12:["어드벤처디자인","공학프로그램응용"],
                 21:["전기회로실험","전자기학1","물리전자공학1","회로이론1","C언어및자료구조"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","객체지향프로그래밍","전자기학2","물리전자공학2","회로이론2"],
                 31:["초고주파공학","전자회로1","전기기계1","전력공학1","전기전자재료공학"],
                 32:["전자회로실험","전자회로2","전기기계2","전력공학2","고전압공학"],
                 41:["캡스톤디자인","전력전자공학","전력시스템응용","전자에너지변환공학","전기설비공학개론"],
                 42:["신재생에너지","분산전원시스템","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE6.insert_last(subj_name="어드벤처디자인",grade=11);EE6.insert_last(subj_name="어드벤처디자인",grade=12);EE6.insert_last(subj_name="공학프로그램응용",grade=12)
EE6.insert_last(subj_name="회로이론1",grade=21);EE6.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE6.insert_last(subj_name="전자기학1",grade=21);EE6.insert_last(subj_name="물리전자공학1",grade=21);EE6.insert_last(subj_name="C언어및자료구조",grade=21)
EE6.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE6.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE6.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["전자기학1"]);EE6.insert_last(subj_name="물리전자공학2",grade=22,prev_subj_nec_names=["물리전자공학1"]);EE6.insert_last(subj_name="객체지향프로그래밍",grade=21,prev_subj_rec_names=["C언어및자료구조"])
EE6.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE6.insert_last(subj_name="전기전자재료공학",grade=31);EE6.insert_last(subj_name="전력공학1",grade=31,prev_subj_rec_names=["회로이론2","전자기학1","전기전자재료공학"]);EE6.insert_last(subj_name="전기기계1",grade=31);EE6.insert_last(subj_name="초고주파공학",grade=31,prev_subj_rec_names=["전자기학2"])
EE6.insert_last(subj_name="전자회로2",grade=32,prev_subj_rec_names=["전자회로1"]);EE6.insert_last(subj_name="고전압공학",grade=32);EE6.insert_last(subj_name="전력공학2",grade=32,prev_subj_rec_names=["고전압공학"],prev_subj_nec_names=["전력공학1"]);EE6.insert_last(subj_name="전자회로실험",grade=32,prev_subj_rec_names=["전자회로1"]);EE6.insert_last(subj_name="전기기계2",grade=32,prev_subj_nec_names=["전기기계1"])
EE6.insert_last(subj_name="캡스톤디자인",grade=41);EE6.insert_last(subj_name="전기설비공학개론",grade=41,prev_subj_rec_names=["전기기계1"]);EE6.insert_last(subj_name="전력시스템응용",grade=41,prev_subj_rec_names=["전기설비공학개론"]);EE6.insert_last(subj_name="전력전자공학",grade=41,prev_subj_rec_names=["전력공학2","전자회로2"]);EE6.insert_last(subj_name="전자에너지변환공학",grade=41,prev_subj_rec_names=["전기기계2"])
EE6.insert_last(subj_name="분산전원시스템",grade=42,prev_subj_rec_names=["전력공학1"]);EE6.insert_last(subj_name="신재생에너지",grade=42);EE6.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE6.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE6.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)

samplesEE6_1=EE6.random_sampling(75,n1=1,n2=1,n3=4,n4=4,n5=4,n6=4,n7=3,n8=2)
samplesEE6_2=EE6.random_sampling(75,n1=0,n2=2,n3=3,n4=4,n5=5,n6=4,n7=3,n8=2)
samplesEE6_3=EE6.random_sampling(75,n1=1,n2=1,n3=3,n4=3,n5=4,n6=3,n7=2,n8=2)
samplesEE6_4=EE6.random_sampling(75,n1=1,n2=0,n3=5,n4=3,n5=4,n6=4,n7=2,n8=3)

EE7=study_system()
EE7.name2id={"회로이론1":"ENE2002","디지털공학":"ENE2003","물리전자공학1":"ENE2005","전자기학1":"ENE2006","전기회로실험":"ENE2007","회로이론2":"ENE2008","논리회로설계":"ENE2009","물리전자공학2":"ENE2011","전자기학2":"ENE2012","디지털실험":"ENE2013","C언어및자료구조":"ENE2015","신호및시스템":"ENE2016","공학프로그램응용":"ENE2017","객체지향프로그래밍":"ENE2018","어드벤처디자인":"ENE2019","마이크로프로세서응용및실험":"ENE4002","고체전자소자":"ENE4004","전력공학1":"ENE4006","전기기계1":"ENE4007","전기전자재료공학":"ENE4008","컴퓨터구조및설계":"ENE4010","디지털신호처리및설계":"ENE4014","전력공학2":"ENE4016","전기기계2":"ENE4017","고전압공학":"ENE4018","SoC설계":"ENE4019","광전자공학":"ENE4024","디지털집적회로설계":"ENE4025","전력전자공학":"ENE4026","전자에너지변환공학":"ENE4027","로봇공학":"ENE4031","반도체공정":"ENE4033","전동력제어및응용":"ENE4035","캡스톤디자인":"ENE4039","랜덤신호이론":"ENE4044","전자회로2":"ENE4045","통신이론":"ENE4046","전기응용":"ENE4049","나노전자기계공학":"ENE4050","전력시스템응용":"ENE4054","분산전원시스템":"ENE4055","신재생에너지":"ENE4056","영상및딥러닝프로그래밍":"ENE4059","영상처리":"ENE4060","디지털통신":"ENE4061","기계학습론":"ENE4062","전자회로1":"ENE4063","전자회로실험":"ENE4064","제어공학개론":"ENE4066","현대제어공학":"ENE4067","아날로그집적회로":"ENE4068","임베디드신호처리시스템":"ENE4069","초고주파공학":"ENE4070","안테나공학":"ENE4071","IoT통신및실습":"ENE4072","전기설비공학개론":"ENE4073","센서응용공학":"ENE4074","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","다학제캡스톤디자인":"DES4009","기업사회맞춤형캡스톤디자인2":"DES4025","기술창업캡스톤디자인2":"DES4032"}
EE7.grade2names={11:["어드벤처디자인"],12:["공학프로그램응용","어드벤처디자인"],
                 21:["전기회로실험","C언어및자료구조","전자기학1","물리전자공학1","회로이론1"],
                 22:["산학융합종합설계(인공지능을 활용한 콘텐츠 제작)","객체지향프로그래밍","전자기학2","물리전자공학2","회로이론2"],
                 31:["마이크로프로세서응용및실험","고체전자소자","전자회로1","전기기계1","전력공학1"],
                 32:["전자회로실험","전자회로2","전기기계2","전력공학2","고전압공학","센서응용공학"],
                 41:["캡스톤디자인","광전자공학","전력전자공학","전력시스템응용","전자에너지변환공학","전기설비공학개론"],
                 42:["임베디드신호처리시스템","전동력제어및응용","전기응용","다학제캡스톤디자인","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2"]}
EE7.insert_last(subj_name="어드벤처디자인",grade=11);EE7.insert_last(subj_name="어드벤처디자인",grade=12);EE7.insert_last(subj_name="공학프로그램응용",grade=12)
EE7.insert_last(subj_name="회로이론1",grade=21);EE7.insert_last(subj_name="전기회로실험",grade=21,prev_subj_rec_names=["회로이론1"]);EE7.insert_last(subj_name="전자기학1",grade=21);EE7.insert_last(subj_name="C언어및자료구조",grade=21);EE7.insert_last(subj_name="물리전자공학1",grade=21)
EE7.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22);EE7.insert_last(subj_name="회로이론2",grade=22,prev_subj_nec_names=["회로이론1"]);EE7.insert_last(subj_name="전자기학2",grade=22,prev_subj_nec_names=["회로이론1"]);EE7.insert_last(subj_name="물리전자공학2",grade=22,prev_subj_nec_names=["물리전자공학1"]);EE7.insert_last(subj_name="객체지향프로그래밍",grade=22,prev_subj_rec_names=["C언어및자료구조"])
EE7.insert_last(subj_name="전자회로1",grade=31,prev_subj_rec_names=["회로이론2"]);EE7.insert_last(subj_name="전력공학1",grade=31,prev_subj_rec_names=["전자기학2"]);EE7.insert_last(subj_name="전기기계1",grade=31,prev_subj_rec_names=["전자기학2"]);EE7.insert_last(subj_name="마이크로프로세서응용및실험",grade=31,prev_subj_rec_names=["C언어및자료구조"]);EE7.insert_last(subj_name="고체전자소자",grade=31,prev_subj_rec_names=["물리전자공학2"])
EE7.insert_last(subj_name="전자회로2",grade=32,prev_subj_nec_names=["전자회로1"]);EE7.insert_last(subj_name="센서응용공학",grade=32);EE7.insert_last(subj_name="전력공학2",grade=32,prev_subj_nec_names=["전력공학1"]);EE7.insert_last(subj_name="전기기계2",grade=32,prev_subj_nec_names=["전기기계1"]);EE7.insert_last(subj_name="전자회로실험",grade=32,prev_subj_rec_names=["전자회로1"]);EE7.insert_last(subj_name="고전압공학",grade=32,prev_subj_rec_names=["전력공학2"])
EE7.insert_last(subj_name="캡스톤디자인",grade=41);EE7.insert_last(subj_name="전자에너지변환공학",grade=41,prev_subj_rec_names=["전기기계2"]);EE7.insert_last(subj_name="전력전자공학",grade=41,prev_subj_rec_names=["센서응용공학","전력공학2","전자에너지변환공학"]);EE7.insert_last(subj_name="전기설비공학개론",grade=41);EE7.insert_last(subj_name="전력시스템응용",grade=41,prev_subj_rec_names=["전기설비공학개론","전력공학1"]);EE7.insert_last(subj_name="광전자공학",grade=41,prev_subj_rec_names=["고체전자소자"])
EE7.insert_last(subj_name="임베디드신호처리시스템",grade=42);EE7.insert_last(subj_name="전기응용",grade=42,prev_subj_rec_names=["전기설비공학개론","전자에너지변환공학","전기기계1"]);EE7.insert_last(subj_name="전동력제어및응용",grade=42,prev_subj_rec_names=["임베디드신호처리시스템","전력전자공학","전기응용"]);EE7.insert_last(subj_name="다학제캡스톤디자인",grade=42);EE7.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);EE7.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42)
samplesEE7_1=EE7.random_sampling(75,n1=1,n2=1,n3=4,n4=4,n5=4,n6=5,n7=4,n8=3)
samplesEE7_2=EE7.random_sampling(75,n1=0,n2=2,n3=5,n4=4,n5=5,n6=4,n7=5,n8=4)
samplesEE7_3=EE7.random_sampling(75,n1=1,n2=1,n3=3,n4=3,n5=5,n6=5,n7=5,n8=2)
samplesEE7_4=EE7.random_sampling(75,n1=1,n2=0,n3=4,n4=3,n5=4,n6=4,n7=4,n8=4)

AllsamplesEE=[]
EElist=[samplesEE1_1,samplesEE1_2,samplesEE1_3,samplesEE2_1,samplesEE2_2,samplesEE2_3,samplesEE3_1,samplesEE3_2,samplesEE3_3,
        samplesEE4_1,samplesEE4_2,samplesEE4_3,samplesEE5_1,samplesEE5_2,samplesEE5_3,samplesEE5_4,samplesEE6_1,samplesEE6_2,samplesEE6_3,samplesEE6_4,
        samplesEE7_1,samplesEE7_2,samplesEE7_3,samplesEE7_4]
for eedataset in EElist:
    AllsamplesEE.extend(eedataset)
print("전체 전전 샘플 수 : ",len(AllsamplesEE))

#정보통신공학 데이터 생성

#딥러닝,통신시스템소프트웨어 빼고 하기
ICE = study_system()
ICE.name2id = {"ICT와소프트웨어":"INC2034","어드벤쳐디자인":"INC2033","정보통신프로그래밍":"INC2031","자료구조와실습":"INC2027","정보통신수학및실습":"INC2025","컴퓨터구성":"INC2028","객체지향언어와실습":"INC2029","컴퓨터알고리즘및실습":"INC2024","확률및랜덤프로세스":"INC2021","신호와시스템":"INC2032",
               "운영체제":"INC4059","암(ARM)마이크로프로세서어셈블리언어프로그래밍":"INC4089","데이터통신":"INC4058","디지털신호처리":"INC4061","통신이론":"INC4110",
               "모바일소프트웨어":"INC4104","임베디드시스템":"INC4086","데이터베이스체제":"INC4057","컴퓨터네트워크":"INC4063","디지털영상처리":"INC4100","디지털통신":"INC4111","커리어멘토링":"DES2001",
               "소프트웨어공학및설계":"INC4093","머신러닝":"INC4096","지능형IoT플랫폼및특허분석":"INC4113","네트워크프로그래밍":"INC4109","데이터압축":"INC4101","무선통신및실험":"INC4070","캡스톤디자인1":"INC4084",
               "네트워크보안":"INC4082","지능형IoT시스템설계및지식재산권":"INC3113","암호알고리즘및응용":"INC4106",
               "산학융합종합설계(인공지능을 활용한 콘텐츠 제작)":"DES2003","산학융합종합설계(지식경영 프로젝트)":"INC4108","캡스톤디자인2":"INC4085","기술창업캡스톤디자인2":"DES4032","기업사회맞춤형캡스톤디자인2":"DES4025","다학제캡스톤디자인":"DES4009"}
ICE.grade2names = {11:["ICT와소프트웨어"],
                   12:["어드벤쳐디자인","정보통신프로그래밍"],
                   21:["자료구조와실습","정보통신수학및실습"],
                   22:["컴퓨터구성","객체지향언어와실습","컴퓨터알고리즘및실습","확률및랜덤프로세스","신호와시스템","산학융합종합설계(인공지능을 활용한 콘텐츠 제작)"],
                   31:["운영체제","암(ARM)마이크로프로세서어셈블리언어프로그래밍","데이터통신","디지털신호처리","통신이론","커리어멘토링"],
                   32:["모바일소프트웨어","임베디드시스템","데이터베이스체제","컴퓨터네트워크","디지털영상처리","디지털통신"],
                   41:["소프트웨어공학및설계","머신러닝","지능형IoT플랫폼및특허분석","네트워크프로그래밍","데이터압축","무선통신및실험","캡스톤디자인1"],
                   42:["네트워크보안","지능형IoT시스템설계및지식재산권","암호알고리즘및응용","산학융합종합설계(지식경영 프로젝트)","캡스톤디자인2","기술창업캡스톤디자인2","기업사회맞춤형캡스톤디자인2","다학제캡스톤디자인"]}

ICE.insert_last(subj_name="ICT와소프트웨어",grade=11);
ICE.insert_last(subj_name="어드벤쳐디자인",grade=12);ICE.insert_last(subj_name="정보통신프로그래밍",grade=12)
ICE.insert_last(subj_name="자료구조와실습",grade=21,prev_subj_nec_names=["어드벤쳐디자인"]);ICE.insert_last(subj_name="정보통신수학및실습",grade=21)
ICE.insert_last(subj_name="컴퓨터구성",grade=22,prev_subj_rec_names=["자료구조와실습"]);ICE.insert_last(subj_name="객체지향언어와실습",grade=22);ICE.insert_last(subj_name="컴퓨터알고리즘및실습",grade=22);ICE.insert_last(subj_name="확률및랜덤프로세스",grade=22);ICE.insert_last(subj_name="신호와시스템",grade=22);ICE.insert_last(subj_name="산학융합종합설계(인공지능을 활용한 콘텐츠 제작)",grade=22)
ICE.insert_last(subj_name="운영체제",grade=31,prev_subj_nec_names=["컴퓨터구성"]);ICE.insert_last("암(ARM)마이크로프로세서어셈블리언어프로그래밍",grade=31);ICE.insert_last("데이터통신",grade=31);ICE.insert_last("디지털신호처리",grade=31,prev_subj_nec_names=["신호와시스템"]);ICE.insert_last(subj_name="통신이론",grade=31);ICE.insert_last(subj_name="커리어멘토링",grade=31)
ICE.insert_last(subj_name="모바일소프트웨어",grade=32,prev_subj_nec_names=["자료구조와실습"]);ICE.insert_last(subj_name="임베디드시스템",grade=32,prev_subj_nec_names=["암(ARM)마이크로프로세서어셈블리언어프로그래밍"]);ICE.insert_last(subj_name="데이터베이스체제",grade=32);ICE.insert_last(subj_name="컴퓨터네트워크",grade=32,prev_subj_nec_names=["데이터통신"]);ICE.insert_last(subj_name="디지털영상처리",grade=32,prev_subj_rec_names=["디지털신호처리"]);ICE.insert_last(subj_name="디지털통신",grade=32,prev_subj_nec_names=["통신이론"])
ICE.insert_last(subj_name="소프트웨어공학및설계",grade=41,prev_subj_rec_names=["모바일소프트웨어"]);ICE.insert_last(subj_name="머신러닝",grade=41,prev_subj_rec_names=["데이터베이스체제"]);ICE.insert_last(subj_name="지능형IoT플랫폼및특허분석",grade=41);ICE.insert_last(subj_name="네트워크프로그래밍",grade=41,prev_subj_rec_names=["컴퓨터네트워크"]);ICE.insert_last(subj_name="데이터압축",grade=41,prev_subj_rec_names=["디지털영상처리"]);ICE.insert_last(subj_name="무선통신및실험",grade=41,prev_subj_rec_names=["디지털통신"]);ICE.insert_last(subj_name="캡스톤디자인1",grade=41)
ICE.insert_last(subj_name="네트워크보안",grade=42);ICE.insert_last(subj_name="지능형IoT시스템설계및지식재산권",grade=42,prev_subj_rec_names=["지능형IoT플랫폼및특허분석"]);ICE.insert_last(subj_name="암호알고리즘및응용",grade=42);ICE.insert_last(subj_name="산학융합종합설계(지식경영 프로젝트)",grade=42);ICE.insert_last(subj_name="캡스톤디자인2",grade=42);ICE.insert_last(subj_name="기술창업캡스톤디자인2",grade=42);ICE.insert_last(subj_name="기업사회맞춤형캡스톤디자인2",grade=42);ICE.insert_last(subj_name="다학제캡스톤디자인",grade=42);
#여기 샘플링하는 것부터 다시!
samplesICE_1=ICE.random_sampling(400,n1=1,n2=1,n3=2,n4=6,n5=5,n6=4,n7=3,n8=3)
samplesICE_2=ICE.random_sampling(400,n1=1,n2=2,n3=1,n4=4,n5=6,n6=5,n7=4,n8=4)
samplesICE_3=ICE.random_sampling(400,n1=1,n2=1,n3=1,n4=5,n5=5,n6=4,n7=5,n8=2)
samplesICE_4=ICE.random_sampling(400,n1=1,n2=2,n3=2,n4=6,n5=4,n6=5,n7=4,n8=4)
samplesICE_5=ICE.random_sampling(400,n1=1,n2=1,n3=1,n4=4,n5=5,n6=3,n7=3,n8=3)
samplesICE_6=ICE.random_sampling(400,n1=1,n2=2,n3=2,n4=3,n5=4,n6=3,n7=4,n8=4)

AllsamplesICE=[]
ICElist=[samplesICE_1,samplesICE_2,samplesICE_3,samplesICE_4,samplesICE_5,samplesICE_6]
for icedataset in ICElist:
    AllsamplesICE.extend(icedataset)
print("전체 정통 샘플 수 : ",len(AllsamplesICE))

#데이터셋 하나로 합치기 시작
#각 샘플마다 속한 학과 추가
i=0
AllsamplesEE_excel=[]
for data in AllsamplesEE:
    data.insert(0,"전자전기공학과")
    AllsamplesEE_excel.append(data)
AllsamplesISE_excel=[]
for data in AllsamplesISE:
    data.insert(0,"산업시스템공학과")
    AllsamplesISE_excel.append(data)
AllsamplesICE_excel=[]
for data in AllsamplesICE:
    data.insert(0,"정보통신공학과")
    AllsamplesICE_excel.append(data)

print("엑셀에 넣을 전전 샘플 개수:",len(AllsamplesEE_excel))
print("엑셀에 넣을 산시 샘플 개수:",len(AllsamplesISE_excel))
print("엑셀에 넣을 정통 샘플 개수:",len(AllsamplesISE_excel))

Excel_data_set = []
Excel_data_set.extend(AllsamplesEE_excel)
Excel_data_set.extend(AllsamplesISE_excel)
Excel_data_set.extend(AllsamplesICE_excel)
#2. 모든 길이를 최대 길이로 패딩
max_length = max(len(sample) for sample in Excel_data_set)
Excel_data_set = [sample + [None] * (max_length - len(sample)) for sample in Excel_data_set]

#print(Excel_data_set[0:5])
print(Excel_data_set[3000:3010])
print("액셀에 들어갈 샘플 개수 : ",len(Excel_data_set))

# Excel_data_set을 데이터 프레임으로 바꾸고 excel로 변환
import pandas as pd
Excel_data_set = pd.DataFrame(Excel_data_set)
excel_filename = "/mnt/c/Users/USER/OneDrive/바탕 화면/융합 소프트웨어/오픈소스소프트웨어프로젝트/팀프로젝트/OSSProj.ver2.0/dl/sample_classes.xlsx"
Excel_data_set.to_excel(excel_filename,index=False)
