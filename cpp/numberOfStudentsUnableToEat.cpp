/*
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
*/

class Student {
    public:
        Student* next = nullptr;
        int pref;

        Student(int val){
            pref = val;
        }
};

class Q {
    public:
        Student* left = nullptr;
        Student* right = nullptr;
        Student* head = nullptr;
        Student* tail = nullptr;
        Student* curr = nullptr;
        int size = 0;

        Q(){
            left = new Student(-1);
            right = new Student(-1);
            left->next = right;
            right->next = nullptr;
        }

        void enqueue(int val){
            curr = new Student(val);
            curr->next = right;

            //If empty
            if (size == 0){
                head = curr;
                tail = curr;
                left->next = curr;
            }
            
            else{
                tail->next  = curr;
                left->next = curr;
                tail = curr;
            }

            size ++;
        }

        int dequeue(){
            //If empty
            if (size == 0){
                return -1;
            }

            curr = head;
            int val = curr->pref;

            if (size == 1){
                left->next = right;
                head = nullptr;
                tail = nullptr;
            }
            else{
                left->next = head->next;
                head = head->next;
                delete curr;
            }
                        
            size --;
            return val;
        }

        void sendToEnd(){
            //Only makes sense if there are more than 1 students
            if(size > 1){
                curr = head;
                left->next = head->next;
                head = left->next;
                curr->next = right;
                tail->next = curr;
                tail = curr;
            }
        }

        int getPreference(){
            if (size>0){
                return head->pref;
            }
            return -1;
        }

        int getSize(){
            return size;
        }

        bool eat(int val){
            if (size==0){
                return true;
            }
            curr = head;
            int iters = 0;

            while(iters < size){
                if (getPreference() == val){
                    //Found!
                    dequeue();
                    return true;
                }
                sendToEnd();
                iters ++;
            }
            return false;
        }
};


class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        //Create student queue
        Q* q = new Q();
        for (auto s:students){
            q->enqueue(s);
        }

        for (int i=0; i<sandwiches.size(); i++){
            bool everyoneAte = q->eat(sandwiches[i]);
            if (everyoneAte == false){
                break;
            }
        }

        int hungryStudentCount = q->getSize();

        return hungryStudentCount;
    }
};
