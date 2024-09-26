/*
https://leetcode.com/problems/design-linked-list/
*/
class Node{
    public:
        int val;
        Node* next;
        Node* prev;

        Node(int val_){
            val = val_;
            next = nullptr;
            prev = nullptr;
        }
};

class MyLinkedList {
    private:
        Node* head = nullptr;
        Node* tail = nullptr;
public:
    MyLinkedList() {

    }
    
    int get(int index) {
        Node* curr = head;
        int idx = -1;

        while (curr != nullptr){
            idx ++;
            if (idx == index){
                return curr->val;
            }
            curr = curr->next;
        }

        return -1;
    }
    
    void addAtHead(int val) {
        Node* newNode = new Node(val);

        if (head == nullptr){
            head = tail = newNode;
            return;
        }
        
        newNode->next = head;
        newNode->prev = nullptr; //not needed tho, by default the constructor puts this to null
        head->prev = newNode;
        head = newNode;
    }
    
    void addAtTail(int val) {
        Node* newNode = new Node(val);

        if (tail == nullptr){
            head = tail = newNode;
            return;
        }

        newNode->next = nullptr;    //not needed tho, by default the constructor puts this to null
        newNode->prev = tail; 
        tail->next = newNode;
        tail = newNode;
    }
    
    void addAtIndex(int index, int val) {
        if (index == 0){
            addAtHead(val);
            return;
        }

        Node* curr = head;
        int idx = -1;

        while (curr != nullptr){
            idx ++;
            if (idx == index){
                Node* newNode = new Node(val);;
                Node* prev = curr->prev;
                newNode->prev = prev;
                newNode->next = curr;
                prev->next = newNode;
                curr->prev = newNode;
                return;
            }

            curr = curr->next;

            if (curr == nullptr && idx + 1 == index){
                addAtTail(val);
                return;
            }
        }
    }
    
    void deleteAtIndex(int index) {
        if (index == 0){
            if (head == nullptr){
                return;
            }
            Node* forward = head->next;
            if (forward != nullptr){
                forward->prev = nullptr;
            }
            head = forward;
            if(head == nullptr){
                tail = nullptr;
            }
            return;
        }

        Node* curr = head;
        int idx = -1;

        while (curr != nullptr){
            idx ++;
            if (idx == index){
                Node* prev = curr->prev;
                Node* forward = curr->next;
                if (forward != nullptr)
                    forward->prev = prev;
                if (prev != nullptr)
                    prev->next = forward;
                if (curr == tail)
                    tail = prev;
                return; 
            }

            curr = curr->next;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */