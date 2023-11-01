from study_system import study_system

ISE=study_system()#ISE=IndustrialSystemsEngineering(산업시스템공학)
ISE.name2id={"인간공학":"ISE2023","데이터분석입문":"ISE2021","3D모델링":"ISE2025","산업시스템프로그래밍1":"ISE2024","어드벤처디자인":"ISE2022","경영과학1":"ISE2016","산업시스템공학의이해":"ISE2018","응용통계학":"ISE2017","정보시스템분석설계":"ISE2024","생산및운영관리":"ISE4002","첨단제조공학":"ISE4005","금융공학입문":"ISE4008","프로젝트관리":"ISE4011","경영과학2":"ISE4014","유통물류관리":"ISE4018","UI/UX설계":"ISE4044","시뮬레이션과응용":"ISE4021","제품개발":"ISE4022","기술경영":"ISE4023","산업시스템공학종합설계":"ISE4026","산업시스템프로그래밍2":"ISE4047","서비스공학":"ISE4029","정보시스템통합및실습":"ISE4032","머신러닝1":"ISE4045","머신러닝2":"ISE4046","헬스케어공학":"ISE4036","실험계획법":"ISE4037","품질공학":"ISE4038","데이터어낼리틱스":"ISE4041","산업AI":"ISE4042","캡스톤디자인대회":"other"}#캡스톤디자인대회는 비교과과정이라 id가 없어 이렇게 설정했음
ISE.grade2names={11:["산업시스템공학의이해"],12:["어드벤처디자인"],21:["응용통계학","인간공학","3D모델링","산업시스템프로그래밍1"],22:["경영과학1","데이터분석입문","정보시스템분석설계"],31:["금융공학입문","경영과학2","머신러닝1","실험계획법","생산및운영관리"],32:["품질공학","첨단제조공학","머신러닝2","기술경영","유통물류관리","헬스케어공학","산업시스템프로그래밍2"],41:["서비스공학","프로젝트관리","시뮬레이션과응용","데이터어낼리틱스","정보시스템통합및실습","산업시스템공학종합설계"],42:["제품개발","UI/UX설계","산업AI","캡스톤디자인대회"]}
#산업시스템공학과 이수체계도 만들기
ISE.insert_last(subj_name="산업시스템공학의이해",grade=11)
ISE.insert_last(subj_name="어드벤처디자인",grade=12,prev_subj_rec_names=["산업시스템공학의이해"])
ISE.insert_last(subj_name="응용통계학",grade=21,Sim_Subj=["확률및통계학"]);ISE.insert_last(subj_name="3D모델링",grade=21);ISE.insert_last(subj_name="인간공학",grade=21);ISE.insert_last(subj_name="산업시스템프로그래밍1",grade=21)
ISE.insert_last(subj_name="경영과학1",grade=22);ISE.insert_last("데이터분석입문",grade=22,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="정보시스템분석설계",grade=22)
ISE.insert_last(subj_name="경영과학2",grade=31,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="실험계획법",grade=31,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="머신러닝1",grade=31,prev_subj_rec_names=["데이터분석입문"]);ISE.insert_last(subj_name="생산및운영관리",grade=31);ISE.insert_last(subj_name="금융공학입문",grade=31,prev_subj_nec_names=["응용통계학"])
ISE.insert_last(subj_name="품질공학",grade=32,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="첨단제조공학",grade=32);ISE.insert_last(subj_name="머신러닝2",grade=32,prev_subj_rec_names="머신러닝1");ISE.insert_last(subj_name="기술경영",grade=32,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="유통물류관리",grade=32,prev_subj_nec_names=["생산및운영관리","경영과학1"]);ISE.insert_last(subj_name="헬스케어공학",grade=32,prev_subj_rec_names=["인간공학"]);ISE.insert_last(subj_name="산업시스템프로그래밍2",grade=32,prev_subj_rec_names=["산업시스템프로그래밍1"])
ISE.insert_last(subj_name="서비스공학",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="프로젝트관리",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="시뮬레이션과응용",grade=41,prev_subj_nec_names=["응용통계학"]);ISE.insert_last(subj_name="데이터어낼리틱스",grade=41,prev_subj_rec_names=["머신러닝1","머신러닝2"]);ISE.insert_last(subj_name="정보시스템통합및실습",grade=41,prev_subj_rec_names=["정보시스템분석설계"]);ISE.insert_last(subj_name="산업시스템공학종합설계",grade=41,prev_subj_nec_names=["산업시스템공학의이해","어드벤처디자인","응용통계학","산업시스템프로그래밍1","경영과학1"])
ISE.insert_last(subj_name="제품개발",grade=42);ISE.insert_last(subj_name="UI/UX설계",grade=42,prev_subj_rec_names=["인간공학","정보시스템분석설계"]);ISE.insert_last(subj_name="산업AI",grade=42,prev_subj_rec_names=["정보시스템분석설계"]);ISE.insert_last(subj_name="캡스톤디자인대회",grade=42)

samples=ISE.random_sampling(10,n1=1,n2=1,n3=3,n4=2,n5=3,n6=5,n7=4,n8=2)
print(samples[0])
print(samples[1])