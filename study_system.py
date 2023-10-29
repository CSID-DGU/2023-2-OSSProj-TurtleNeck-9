import random

class study_system:    
    class Node:
        def __init__(self,Subj_Name="",Subj_ID="",grade=0,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=list()):
            self.Prev_Subj_nec = Prev_Subj_nec#선이수 과목 리스트(Node 객체 리스트) - 이들을 전부 들었을 때만 이 과목 들을 수 있도록 연결할 것
            self.Prev_Subj_rec = Prev_Subj_rec#권장 선이수
            self.Sim_Subj= list()#비슷한 과목 리스트(이름 or 과목id 리스트로 할 것)
            self.After_Subj = After_Subj#이 과목 이후에 들을 과목(이후, insert할 때, 이 Prev_Subj, After_Subj가 채워질 것)
            
            self.grade = grade#학년(몇학년짜기 수업인지)
            self.Subj_Name = Subj_Name#이 과목 이름
            self.Subj_ID = Subj_ID#이 과목의 ID
    
    def __init__(self):
        self.head = self.Node();self.tail = self.Node(prev_Subj_nec=[self.head]);self.head.After_Subj.append(self.tail)#시작은 head와 tail이 서로 연결되어 있는 상태
        self.name2id = dict()#처음 객체 만들었을 때, 이것 2개부터 채우기!
        self.grade2names= dict()#각 학년 별로 과목 리스트(즉, value는 list)
        #이후, 실제 이수체계도 만들 땐, 이 함수만으로 할 것이기에 과목들을 무조건 순서대로(1~4, 선수, 비선수...) insert해야됨!
    
    def search_by_id(self,start_node,subj_id):#이 id에 해당하는 노드 찾기(by 전위순회-node x 도착 시, x먼저 방문) / 우리가 search시작하는 node는 왠만해선 self.head임!
        if subj_id not in self.name2id.values():#오류 낼 경우(없는 id일 경우), none 값 출력하도록 한 것
            return None
        else:#id가 존재할 경우, 이 전위순회는 무조건 멈추게 할 수 있으니, 이렇게 subj_id 있는지 여부부터 본 것
            if start_node != self.tail:
                if start_node.Subj_ID==subj_id:
                    answer_node=start_node
                else:
                    for subj_node in start_node.After_Subj:#이 start_node가 정답 x이면, 이 하위 노드들로 이동
                        answer_node=self.search_by_id(subj_node,subj_id)
                        if answer_node.Subj_ID==subj_id:
                            break#만약 정답을 이 start_node의 하위 노드들(start_node.After_Subj) 중에 찾았다면, 더이상 for문을 진행x, 상위노드로 head까지 쭉 이 answer node값 유지하기 위해 이 문장 쓴 것
            else:#tail이 start node일 경우
                answer_node=None#이렇게 되면, tail 만나기 전까지 계속 "self.search_by_id(subj_node,subj_id)" 호출되다가 tail이 start_node가 되면, -> None이 return
            return answer_node#그래서 None이 계속 answer_node가 되어 상위 노드가 start_node일 때도 return은 None이었다가 정답 만나면, for문 실행 중단 -> "self.search_by_id(subj_node,subj_id)" 호출 중단 and 이 정답 노드 주소가 return 값이 되고, 위 break문에 의해 처음 호출된 메서드까지 이 값 유지됨.
        
    
    def insert_last(self,subj_name,subj_id,grade,prev_subj_ids=list()):#prev_subj인 id들을 모두 dictionary에서 찾기(사이트에 있는 이수체계도 참고) -> prev_subj_ids(list)
        #작동 방식 : 해당 과목(subj_name) 듣기 직전 수강과목들을 모두 찾기(by prev_subj_ids-> 노드 각각 한개씩 찾아 새로운 노드를 이후 노드(After_Subj) 리스트에 추가 )
        #새 노드 생성->by for문, 각 prev_subj_ids마다 search -> 해당 노드 return -> 이 노드의 After_Subj list에 새 노드 append and 새 노드의 Prev_Subj_nec에는 return된 노드 append 
        if subj_id not in self.name2id.values() or subj_name not in self.name2id.keys():
            print("전공에 알맞은 과목이 아닙니다. dictionary name2id에 등록된 과목인지 확인하기")
        else:
            new_subj_node=self.Node(Subj_Name=subj_name,Subj_ID=subj_id,grade=grade,After_Subj=list(),Prev_Subj_rec=list())
            new_subj_node.After_Subj.append(self.tail)#마지막 계층의 자식노드가 추가되는 것이니, tail과 연결
            for id in prev_subj_ids:#선수과목들에게 이후 들을 과목 list에 추가하는 것
                prev_node=self.search_by_id(self.head,id)
                if self.tail in prev_node.After_Subj:#prev_node list에 tail있으면 없애는 코드
                    del prev_node.After_Subj[0]#tail은 가장 마지막 자식 노드들의 After_Subj list 첫번째에 위치하고 있기 때문에 이렇게 짜면 됨(by 밑의 append)
                prev_node.After_Subj.append(new_subj_node)
    
    #colab에서 객체 list 생성후, del, ... in ... 똑바로 작동하는지 확인해보기

    def search_randomsubj_by_grade(self, n, grade):#n:sample로 뽑을 과목 개수, grade : 해당 학년에 속한 과목들 중에 뽑을 것
        subj_names=self.grade2names[grade]#해당 학년에서 n개 뽑힐 과목 후보군
        selected_subj_names=random.sample(subj_names,n)
        selected_subj_names=sorted(selected_subj_names)#정렬해서 sample 만들면, 좀 더 좋은 훈련 가능(이후에)
        selected_subj_nodes=[]
        for name in selected_subj_names:#id로 노드 하나씩 출력할 것
            selected_subj_nodes.append(self.search_by_id(self.name2id[name]))
        return selected_subj_nodes
        #randomsampling에서 최종적으로 이 각 선택된 노드들로부터 선수과목이 내가 뽑은 sample에 있는지 조사 -> 없으면, 그거만 먼저 듣게 하거나, 동시에 듣게 할 것

    #def random_sampling(self,n):#n:만들 sample 개수


        