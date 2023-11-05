import random

class study_system:    
    class Node:
        def __init__(self,Subj_Name="",Subj_ID="",grade=0,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=list(),Sim_Subj=list()):
            self.Prev_Subj_nec = Prev_Subj_nec
            self.Prev_Subj_rec = Prev_Subj_rec
            self.Sim_Subj= Sim_Subj
            self.After_Subj = After_Subj
            
            self.grade = grade
            self.Subj_Name = Subj_Name
            self.Subj_ID = Subj_ID
    
    def __init__(self):
        self.head = self.Node(Subj_Name="head",Subj_ID="start");self.tail = self.Node(Subj_Name="tail",Subj_ID="end",Prev_Subj_nec=[self.head])
        self.head.After_Subj=[self.tail]
        self.name2id = dict()
        self.grade2names= dict()
    
    def search_by_id(self,start_node,subj_id):
        if subj_id not in self.name2id.values():
            print("전공 관련된 과목id 아님. dictionary name2id 확인하기")
            return None
        else:
            if start_node != self.tail:
                if start_node.Subj_ID==subj_id:
                    answer_node=start_node
                else:
                    for subj_node in start_node.After_Subj:
                        answer_node=self.search_by_id(subj_node,subj_id)
                        if answer_node.Subj_ID==subj_id:
                            break
            else:
                answer_node=self.tail
            return answer_node
        
    
    def insert_last(self,subj_name,grade,prev_subj_nec_names=list(),prev_subj_rec_names=list(),Sim_Subj=list()):
        if subj_name not in self.name2id.keys():
            print("전공에 알맞은 과목이 아닙니다. dictionary name2id에 등록된 과목인지 확인하기")
        else:
            new_subj_node=self.Node(Subj_Name=subj_name,Subj_ID=self.name2id[subj_name],grade=grade,Prev_Subj_nec=list(),After_Subj=list(),Prev_Subj_rec=list(), Sim_Subj=Sim_Subj)
            if len(prev_subj_nec_names)==0:
                new_subj_node.After_Subj.append(self.tail)
                self.tail.Prev_Subj_nec.append(new_subj_node)
                new_subj_node.Prev_Subj_nec.append(self.head)
                self.head.After_Subj.append(new_subj_node)
                if self.tail in self.head.After_Subj:
                    del self.head.After_Subj[self.head.After_Subj.index(self.tail)]
                if self.head in self.tail.Prev_Subj_nec:
                    del self.tail.Prev_Subj_nec[self.tail.Prev_Subj_nec.index(self.head)]
            else:
                new_subj_node.After_Subj.append(self.tail)
                self.tail.Prev_Subj_nec.append(new_subj_node)
                prev_subj_ids=list()
                for name in prev_subj_nec_names:
                    prev_subj_ids.append(self.name2id[name])
                for id in prev_subj_ids:
                    prev_node=self.search_by_id(self.head,id)
                    if self.tail in prev_node.After_Subj:
                        del prev_node.After_Subj[prev_node.After_Subj.index(self.tail)]
                    if prev_node in self.tail.Prev_Subj_nec:
                        del self.tail.Prev_Subj_nec[self.tail.Prev_Subj_nec.index(prev_node)]
                    prev_node.After_Subj.append(new_subj_node)
                    new_subj_node.Prev_Subj_nec.append(prev_node)
            if len(prev_subj_rec_names)==0:
                new_subj_node.Prev_Subj_rec.append(self.head)
            else:
                prev_subj_rec_ids = list()
                for name in prev_subj_rec_names:
                    prev_subj_rec_ids.append(self.name2id[name])
                for id in prev_subj_rec_ids:
                    prev_rec_node = self.search_by_id(self.head,id)
                    new_subj_node.Prev_Subj_rec.append(prev_rec_node)

    def search_randomsubj_by_grade(self, n, grade):
        subj_names=self.grade2names[grade]
        selected_subj_names=random.sample(subj_names,n)
        selected_subj_names=sorted(selected_subj_names)
        selected_subj_nodes=[]
        for name in selected_subj_names:
            selected_subj_nodes.append(self.search_by_id(self.head,self.name2id[name]))

        return selected_subj_nodes

    def find_first_prev_subjs_to_learn(self, subj_node,taken_subjects):
        if subj_node.Prev_Subj_nec[0] == self.head:
            return [subj_node]
        list_subj2learn=[]
        i=0
        prev_subj_names=[prev_subj_node.Subj_Name for prev_subj_node in subj_node.Prev_Subj_nec]
        for prev_subj in prev_subj_names:
            if prev_subj in taken_subjects:
                continue
            else:
                prev_subj_node_p=self.search_by_id(self.head,self.name2id[prev_subj])
                Sim_Subjs_of_prev_subj=[sim_subj for sim_subj in prev_subj_node_p.Sim_Subj]
                exist_sim_subj="None"
                for sim_subj_p in Sim_Subjs_of_prev_subj:
                    if sim_subj_p in taken_subjects:
                        exist_sim_subj=sim_subj_p
                        break
                if exist_sim_subj in taken_subjects:
                    continue
                i+=1
                list_subj2learn.extend(self.find_first_prev_subjs_to_learn(prev_subj_node_p,taken_subjects))
        if i==0:            
            return [subj_node]
        else:
            return list_subj2learn
    def random_sampling(self,iteration,n1,n2,n3,n4,n5,n6,n7,n8):
        samples=list()
        for iter in range(iteration):
            num_subj_each_grade=[n1,n2,n3,n4,n5,n6,n7,n8]
            i=0
            grade_seme = [11,12,21,22,31,32,41,42]
            result=list()
            for num in num_subj_each_grade:
                cnddt=self.search_randomsubj_by_grade(num,grade_seme[i])
                for subj_node in cnddt:
                    subjs2learn_first=self.find_first_prev_subjs_to_learn(subj_node,result)
                    subjs2learn=[]
                    for prev_subj_node in subjs2learn_first:
                        sim_subjs=[subj  for subj in prev_subj_node.Sim_Subj]
                        sim_subjs.append(prev_subj_node.Subj_Name)
                        subj=random.sample(sim_subjs,1)[0]
                        subjs2learn.append(subj)
                    if self.head not in subj_node.Prev_Subj_rec:  
                        prev_subj_rec_names=[prev_subj_rec_node.Subj_Name for prev_subj_rec_node in subj_node.Prev_Subj_rec]
                        Existence_of_prev_subj = "None"
                        for subj_name in prev_subj_rec_names:
                            if subj_name in result:
                                Existence_of_prev_subj = "Yes"
                                break
                            for sim_subj in self.search_by_id(self.head,self.name2id[subj_name]).Sim_Subj:
                                if sim_subj in result:
                                    Existence_of_prev_subj = "Yes"
                                    break
                            if Existence_of_prev_subj == "Yes":
                                break
                        if Existence_of_prev_subj=="None":
                            num2learn_prev_subj_rec=random.randrange(1,len(subj_node.Prev_Subj_rec)+1)
                            subjs_rec_nodes_2learn=random.sample(subj_node.Prev_Subj_rec,num2learn_prev_subj_rec)
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
