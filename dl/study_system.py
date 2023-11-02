import random

class study_system:    
    class Node:
        def __init__(self,Subj_Name="",Subj_ID="",grade=0,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=list(),Sim_Subj=list()):
            self.Prev_Subj_nec = Prev_Subj_nec#선이수 과목 리스트(Node 객체 리스트) - 이들을 전부 들었을 때만 이 과목 들을 수 있도록 연결할 것
            self.Prev_Subj_rec = Prev_Subj_rec#권장 선이수 과목 리스트(Node 객체 리스트)
            self.Sim_Subj= Sim_Subj#비슷한 과목 리스트(이름 or 과목id 리스트로 할 것)
            self.After_Subj = After_Subj#이 과목 이후에 들을 과목들(노드 리스트)(이후, insert할 때, 이 Prev_Subj, After_Subj가 채워질 것)
            
            self.grade = grade#학년(몇학년짜기 수업인지)
            self.Subj_Name = Subj_Name#이 과목 이름
            self.Subj_ID = Subj_ID#이 과목의 ID
    
    def __init__(self):
        self.head = self.Node(Subj_Name="head",Subj_ID="start");self.tail = self.Node(Subj_Name="tail",Subj_ID="end",Prev_Subj_nec=[self.head])
        self.head.After_Subj=[self.tail]#시작은 head와 tail이 서로 연결되어 있는 상태
        self.name2id = dict()#처음 객체 만들었을 때, 이것 2개부터 채우기!
        self.grade2names= dict()#각 학년 별로 과목 리스트(즉, value는 list)
        #이후, 실제 이수체계도 만들 땐, 이 함수만으로 할 것이기에 과목들을 무조건 순서대로(1~4, 선수, 비선수...) insert해야됨!
    
    def search_by_id(self,start_node,subj_id):#이 id에 해당하는 노드 찾기(by 전위순회-node x 도착 시, x먼저 방문(즉, x의 값부터 검사)) / 우리가 search시작하는 node는 왠만해선 self.head임!
        if subj_id not in self.name2id.values():#오류 낼 경우(없는 id일 경우), none 값 출력하도록 한 것
            print("전공 관련된 과목id 아님. dictionary name2id 확인하기")
            return None
        else:#id가 존재할 경우, 이 전위순회는 무조건 멈추게 할 수 있으니, 이렇게 subj_id 있는지 여부부터 본 것
            if start_node != self.tail:
                if start_node.Subj_ID==subj_id:
                    answer_node=start_node
                else:
                    for subj_node in start_node.After_Subj:#이 start_node가 정답 x이면, 이 하위 노드들로 이동(start_node.Subj_ID==subj_id일 때까지 이 for문을 돌며 search_by_id 계속 호출되며 하위 노드로 내려가 tail까지)
                        answer_node=self.search_by_id(subj_node,subj_id)
                        if answer_node.Subj_ID==subj_id:
                            break#만약 정답을 이 start_node의 하위 노드들(start_node.After_Subj) 중에 찾았다면, 더이상 for문을 진행x, 상위노드로 head까지 쭉 이 answer node값 유지하기 위해 이 문장 쓴 것
            else:#tail이 start node일 경우
                answer_node=self.tail#이렇게 되면, tail 만나기 전까지 계속 "self.search_by_id(subj_node,subj_id)" 호출되다가 tail이 start_node가 되면, -> None이 return
            return answer_node#그래서 None이 계속 answer_node가 되어 상위 노드가 start_node일 때도 return은 None이었다가 정답 만나면, for문 실행 중단 -> "self.search_by_id(subj_node,subj_id)" 호출 중단 and 이 정답 노드 주소가 return 값이 되고, 위 break문에 의해 처음 호출된 메서드까지 이 값 유지됨.
        
    
    def insert_last(self,subj_name,grade,prev_subj_nec_names=list(),prev_subj_rec_names=list(),Sim_Subj=list()):#prev_subj인 name들을 모두 dictionary에서 찾아 같은 순서의 id 리스트로 만들기(즉, 같은 index에는 같은 과목에 대한 id, name)
        #작동 방식 : 해당 과목(subj_name) 듣기 직전 수강과목들을 모두 찾기(by prev_subj_ids-> 노드 각각 한개씩 찾아 새로운 노드를 이후 노드(After_Subj) 리스트에 추가 )
        #새 노드 생성->by for문, 각 prev_subj_ids마다 search -> 해당 노드 return -> 이 노드의 After_Subj list에 새 노드 append and 새 노드의 Prev_Subj_nec에는 return된 노드 append 
        #선수과목이 아예 없거나, 1학년 과목의 경우, head(name:head)와 바로 연결
        #Sim_Subj, prev_subj_rec_names 모두 string 리스트로.
        if subj_name not in self.name2id.keys():
            print("전공에 알맞은 과목이 아닙니다. dictionary name2id에 등록된 과목인지 확인하기")
        else:
            new_subj_node=self.Node(Subj_Name=subj_name,Subj_ID=self.name2id[subj_name],grade=grade,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=list(), Sim_Subj=Sim_Subj)
            if len(prev_subj_nec_names)==0:#즉, 선이수 과목이 없는 과목 노드를 추가하고 싶은 경우엔 head,tail와만 연결하면 됨.
            #1. 필수 선이수 관계 연결
                #함수 입력값 보면 알 수 있듯이, 필수 선이수 과목은 id로 노드 search해야 하기에 일단 new node만들 때, 빈 리스트(Prev_Subj_nec=list())로 만들고, 이후에 하나씩 필수 선이수 과목 노드를 id로부터 찾아 넣지만
                #권장 선이수 과목 list(prev_subj_rec_names)와 비슷한 과목 list(Sim_Subj)은 노드에서 string list이기에
                #메서드 호출할 때, 다 입력할 것!
#                new_subj_node=self.Node(Subj_Name=subj_name,Subj_ID=self.name2id[subj_name],grade=grade,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=prev_subj_rec_names, Sim_Subj=Sim_Subj)
                #tail과 양방향 연결
                new_subj_node.After_Subj.append(self.tail)#마지막 계층의 자식노드가 추가되는 것이니, tail과 연결(밑의 줄 포함 - 양방향 연결)
                self.tail.Prev_Subj_nec.append(new_subj_node)
                #head와 양방향 연결
                new_subj_node.Prev_Subj_nec.append(self.head)
                self.head.After_Subj.append(new_subj_node)
                #head와 tail간의 연결 제거(만약 있다면)
                if self.tail in self.head.After_Subj:
                    del self.head.After_Subj[self.head.After_Subj.index(self.tail)]
                if self.head in self.tail.Prev_Subj_nec:
                    del self.tail.Prev_Subj_nec[self.tail.Prev_Subj_nec.index(self.head)]
            else:#선이수 과목이 있는 경우(즉, 선이수 과목 노드 저장되어 있는 상태)
#                new_subj_node=self.Node(Subj_Name=subj_name,Subj_ID=self.name2id[subj_name],grade=grade,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=prev_subj_rec_names, Sim_Subj=Sim_Subj)
                #마지막 계층의 자식노드가 추가되는 것이니, tail과 연결(밑의 줄 포함 - 양방향 연결)
                new_subj_node.After_Subj.append(self.tail)
                self.tail.Prev_Subj_nec.append(new_subj_node)
                #선이수과목 id 찾기 -> 선이수 과목 id 리스트 만들기
                prev_subj_ids=list()
                for name in prev_subj_nec_names:
                    prev_subj_ids.append(self.name2id[name])
                #선이수 과목 id마다 선이수과목 노드 찾고 -> 노드 연결(양방향)
                for id in prev_subj_ids:#선수과목들에게 이후 들을 과목 list에 추가하는 것(new node와 양방향 연결)+그러면서 tail과의 연결 제거(직전 선수과목들은 tail과 연결되어 있을 터이니)
                    prev_node=self.search_by_id(self.head,id)
                    if self.tail in prev_node.After_Subj:#prev_node list에 tail있으면 없애는 코드
                        del prev_node.After_Subj[prev_node.After_Subj.index(self.tail)]
                        #self.tail의 prev_node도 다시 지정하기!(=prev_node 지우고, new_subj_node를 append)
                    if prev_node in self.tail.Prev_Subj_nec:
                        del self.tail.Prev_Subj_nec[self.tail.Prev_Subj_nec.index(prev_node)]#prev_node가 tail의 선수과목에 있으면(즉, tail과 연결되어 있으면), 연결 끊기
                    prev_node.After_Subj.append(new_subj_node)#직전 선수과목들에게 이후 들을 과목으로 new_subj_node 지정
                    new_subj_node.Prev_Subj_nec.append(prev_node)#이 new_subj의 선수과목 연결하기(즉, 양방향 연결)
            #필수 선이수 관계 연결 끝났으면, 권장 선이수관계 연결
            #2. 권장 선이수 관계 연결(단방향 - Prev_Subj_rec은 이후, 들었는지 여부 체크용으로 쓸 것이기에 이전 단계 방향으로 연결하는 것만 하면 됨.)
            if len(prev_subj_rec_names)==0:#해당 과목(subj_name)의 권장 선이수 과목이 없는 경우, 마지막 지점 self.head노드와 연결
                new_subj_node.Prev_Subj_rec.append(self.head)
            else:#권장 선이수 과목 있는 경우
                #권장 선이수 과목 id 각각 찾아 -> id리스트 -> by for문, id로 노드 찾아 Prev_Subj_rec에 append
                prev_subj_rec_ids = list()
                for name in prev_subj_rec_names:
                    prev_subj_rec_ids.append(self.name2id[name])
                for id in prev_subj_rec_ids:
                    prev_rec_node = self.search_by_id(self.head,id)#권장 선이수 과목은 단방향 연결(head쪽)이면 충분
                    new_subj_node.Prev_Subj_rec.append(prev_rec_node)
    #colab에서 객체 list 생성후, del, ... in ... 똑바로 작동하는지 확인해보기

    def search_randomsubj_by_grade(self, n, grade):#n:sample로 뽑을 과목 개수, grade : 해당 학년에 속한 과목들 중에 뽑을 것
        subj_names=self.grade2names[grade]#해당 학년에서 n개 뽑힐 과목 후보군
        selected_subj_names=random.sample(subj_names,n)#n개 random 뽑기
        selected_subj_names=sorted(selected_subj_names)#정렬해서 sample 만들면, 좀 더 좋은 훈련 가능(이후에)
        selected_subj_nodes=[]
        for name in selected_subj_names:#id로 노드 하나씩 출력할 것
            selected_subj_nodes.append(self.search_by_id(self.head,self.name2id[name]))
        return selected_subj_nodes
        #random_sampling에서 최종적으로 이 각 선택된 노드들로부터 선수과목이 내가 뽑은 sample에 있는지 조사 -> 없으면, 그거만 먼저 듣게 하거나, 동시에 듣게 할 것


    def find_first_prev_subjs_to_learn(self, subj_node,taken_subjects):#taken_subjects(이미 들은 subject list)가 주어졌을 때, subj_node의 가장 처음으로 들어야할 subject노드를 return
        #밑의 random_sampling에서 쓰일 때, subj_node=prev_subj_node | taken_subjects=result(subject 이름들(string)의 list)
        #1. subj_node의 모든 필수 선수과목을 들었을 경우, subj_node return
        if subj_node.Prev_Subj_nec[0] == self.head:#더 이상 recursion 할 거 없으니, 이 recursion일어나면 안 되고, 지금의 이 subj_node가 들어야할 과목이라는 뜻!(이 if문 실행시, 이 subj_node의 선수과목 x 의미이니까!)
            return [subj_node]
        list_subj2learn=[]
        i=0
            #subj_node의 모든 필수 선수과목을 뽑아 리스트(prev_subj_names)로 만들고, 이 각 과목+비슷한 과목들 중 하나라도 들었는지 확인(by for문)
        prev_subj_names=[prev_subj_node.Subj_Name for prev_subj_node in subj_node.Prev_Subj_nec]#같은 단계의(즉 여기서prev_subj_names 서로 같이 들을 수 있는 과목들이다.)
        for prev_subj in prev_subj_names:#선이수과목 각각에 대해
            if prev_subj in taken_subjects:#들은 과목 리스트에 있으면, 다음 선이수과목 있는지 검사
                continue
            else:#없으면, 이 prev_subj와 비슷한 과목(Sim_Subj)이 하나로도 있는지 보기 -> 하나라도 있으면 다음 선이수과목 검사 | 없으면 recursion
                prev_subj_node_p=self.search_by_id(self.head,self.name2id[prev_subj])
                Sim_Subjs_of_prev_subj=[sim_subj for sim_subj in prev_subj_node_p.Sim_Subj]#prev_subj_node_p.Sim_Subj은 string list
                exist_sim_subj="None"#비슷한 과목이 taken_subject에 있으면, 그 과목을 exist_sim_subj로 할 것
                for sim_subj_p in Sim_Subjs_of_prev_subj:#만약 비슷한 과목이 없으면 빈 배열이니, 그냥 for문 넘어가게 됨.
                    if sim_subj_p in taken_subjects:
                        exist_sim_subj=sim_subj_p
                        break
                if exist_sim_subj in taken_subjects:#비슷한 과목 찾았으면, 다음 prev_subj에 대해서 검사
                    continue
        #2. 안 들은 필수 선수과목(위 continue를 지나쳐 오면, 안 들은 필수 선수과목 = prev_subj) 남아있은 경우, recursive를 통해 처음으로 들어야할 필수 선수과목들의 node 찾기 
                #Sim_Subj조차도 하나도 taken_subjects에 없으면 이 prev_node를 꼭 들어야 하는데, 안들은 것이니 이 전(prev_node.Prev_Node_nec) 필수 선이수는 들었는지 체크(by recursion)
                i+=1
                #아직 더 이전 과목으로 갈 수 있으면,(prev_subj를 안 들은 경우 더 이전 subj는 들었는지 체크하여 그것을 안들었으면, prev_subj는 못 듣고, 이 subj만 듣게 할 것)
                #이건 가장 최상위 for문과 continue문을 보면 알 수 있겠지만, prev_subj_node_p의 subject인 prev_subj, 이와 비슷한 subj 모두 안 들었을 때, 이 recursion 실행
                list_subj2learn.extend(self.find_first_prev_subjs_to_learn(prev_subj_node_p,taken_subjects))
        #prev_subj모두 들은 상태(모든 prev_subj에 대해서 i+=1이 실행 x 의미!)에서 subj_node인 경우, subj_node가 가장 처음으로 들어야할 subj임!
        if i==0:            
            return [subj_node]
        else:
            return list_subj2learn#가장 처음 시작 노드로서의 subj_node가 입력값일 땐, 즉, 처음 호출되 find_first_prev_subj_to_learn일 땐, 이것이 return된다.

    def random_sampling(self,iteration,n1,n2,n3,n4,n5,n6,n7,n8):#n1:1학년 1학기과목에서 뽑을 과목 수...
        samples=list()
        for iter in range(iteration):#iteration: 뽑을 sample 갯수
            num_subj_each_grade=[n1,n2,n3,n4,n5,n6,n7,n8]
            i=0
            grade_seme = [11,12,21,22,31,32,41,42]#11 = 1학년 1학기
            result=list()#한 샘플이 들은 과목 list(들은 순서대로(name list))
            for num in num_subj_each_grade:
                cnddt=self.search_randomsubj_by_grade(num,grade_seme[i])#grade_seme[i](학년학기) 때 들을 과목 후보군(노드 리스트)
                #이 후보군의 각 필수선수과목에 대해서 학습했는지 파악하기(즉 result에 선수과목 이름 있는지 후보군의 각 노드별로 파악) -> 없으면, 그 선수과목 노드와 이 후보군의 노드 바꾸기(cnddt에서)
                for subj_node in cnddt:
                    #1.필수 선이수 검사(subj_node)
                    subjs2learn_first=self.find_first_prev_subjs_to_learn(subj_node,result)#각 subj_node의 subj의 선수과목 모두 들었으면, [subj_node]출력되게 함.
                    #위 노드 리스트를 문자열 리스트로
                    #subjs2learn_first는 subj_node 듣기 위해 필요한 과목들의 노드들의 리스트로, 만약, result에 이 과목들이 모두 포함되어 있으면, subj_node만이 이 리스트에 들어 있을 것([subj_node])
                    subjs2learn=[]
                    #이 for문은 각 필수 선이수 과목(prev_subj_node)에 대해 비슷한 과목을 포함해서 하나만 골라 
                    #subj_node의 과목을 듣기 위해 필요한 과목들을 모으는 것으로, 만약 이미 필요한 필수 선이수 과목 다 들었으면, prev_subj_node=subj_node임을 기억하기
                    for prev_subj_node in subjs2learn_first:
                        sim_subjs=[subj  for subj in prev_subj_node.Sim_Subj]#string list
                        sim_subjs.append(prev_subj_node.Subj_Name)
                        subj=random.sample(sim_subjs,1)[0]
                        subjs2learn.append(subj)
                    #2. 권장 선이수 검사(subj_node의)
                    #이 자리에 만약 subj_node의 권장 선이수 교과목 들은 것이 하나도 없다면, random으로 0~2개 듣게 하기(즉, subjs2learn_first 자리에 추가!)
                    #즉, 이 subj_node의 Prev_Subj_rec 중 하나도 들은 것이 없다면, Prev_Subj_rec 중 0~len(Prev_Subj_rec)-1개 중 random 개수만큼 Prev_Subj_rec 뽑아 듣게 하기
                    #->이를 하기 위해선 1. Node 클래스에서 Prev_Subj_rec도 nec처럼 Node 객체 리스트로, 2. InsertLast 바꾸기 3. 이 메서드 이 위치에서 바로 rec 있는지 찾고, result에 sim_subj 있는지까지 바로 판단(self.find_first_prev_subjs_to_learn와 달리 recursion까지 할 필요 x - 권장이니까! -> 같이 들을 수 있게 할 것)
                    if self.head not in subj_node.Prev_Subj_rec:#insert_last참고하면 권장 선수 과목 x인 과목 노드들은 Prev_Subj_rec에 self.head 넣어 가리키게 해놨으므로, self.head가 아닌 경우만 이 if문 실행되게 하기
                        #subj_node.Prev_Subj_rec의 각 노드(prev_subj_rec_node)의 과목 or sim_subj 중 하나라도 result에 있는지 확인 -> 없을 땐, random으로 subj2learn에 집어넣을지 결정하기
                        #find_first_prev_subjs_to_learn함수 부분 응용하기    
                        prev_subj_rec_names=[prev_subj_rec_node.Subj_Name for prev_subj_rec_node in subj_node.Prev_Subj_rec]
                        Existence_of_prev_subj = "None"
                        for subj_name in prev_subj_rec_names:
                            if subj_name in result:
                                Existence_of_prev_subj = "Yes"
                                break
                            #subj_name에 대한 학점상호 인정 교과목(sim_subj)도 모두 없는지 확인
                            for sim_subj in self.search_by_id(self.head,self.name2id[subj_name]).Sim_Subj:
                                if sim_subj in result:
                                    Existence_of_prev_subj = "Yes"
                                    break#하나라도 있으면 권장 선이수 들은 것이나 마찬가지 이기에!
                            if Existence_of_prev_subj == "Yes":#해당 권장 선이수 과목과 이의 sim_subj 중 하나라도 들었으면, 권장 선이수 더 이상 추가 안 해도 되게 한 것(Existence_of_prev_subj = "Yes"가 되기에 밑의 if 문 과정 x)
                                break
                        if Existence_of_prev_subj=="None":#권장 선이수 들은 것이 없으면 0~선이수 과목 전부 듣는 선택 중 하나는 하기
                            num2learn_prev_subj_rec=random.randrange(1,len(subj_node.Prev_Subj_rec)+1)#1 이상의 권장 선이수 과목 random으로 선택하여 듣게 하기
                            #subj_node.Prev_Subj_rec에서 num2learn_prev_subj_rec만큼 random으로 선택
                            subjs_rec_nodes_2learn=random.sample(subj_node.Prev_Subj_rec,num2learn_prev_subj_rec)
                            #선택된 각 노드마다 sim_subj와 같이 리스트로 묵어 random으로 하나씩 이름 선택 -> subjs2learn.append하기!
                            subj_rec_names2learn=[]
                            for subj_rec_node in subjs_rec_nodes_2learn:
                                sim_subjs=[subj  for subj in subj_rec_node.Sim_Subj]#string list
                                sim_subjs.append(subj_rec_node.Subj_Name)
                                subj=random.sample(sim_subjs,1)[0]
                                subjs2learn.append(subj)
                    result.extend(subjs2learn)
                i+=1
            samples.append(result)
        return samples
