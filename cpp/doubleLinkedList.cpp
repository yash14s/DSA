/*
https://leetcode.com/problems/design-linked-list/
*/

class Node{
    public:
        int val;
        Node* next;
        Node* prev;

        Node(int data){
            val = data;
            next = nullptr;
            prev = nullptr;
        }
};

class MyLinkedList {
public:
    Node* left;
    Node* right;
    MyLinkedList() {
        left = new Node(0);
        right = new Node(0);
        left->next = right;
        right->prev = left;
    }
    
    int get(int index) {
        int idx = 0;
        Node* curr = left->next;

        while (curr != nullptr){
            if(idx == index && curr != right){
                return curr->val;
            }
            curr = curr->next;
            idx ++;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        Node* node = new Node(val);
        Node* prev = left;
        Node* next = left->next;

        node->next = next;
        node->prev = prev;
        prev->next = node;
        next->prev = node;
    }
    
    void addAtTail(int val) {
        Node* node = new Node(val);
        Node* next = right;
        Node* prev = right->prev;

        node->next = next;
        node->prev = prev;
        prev->next = node;
        next->prev = node;       
    }
    
    void addAtIndex(int index, int val) {
        int idx = 0;
        Node* curr = left->next;

        while (curr != nullptr){
            if(idx == index){
                Node* node = new Node(val);
                Node* next = curr;
                Node* prev = curr->prev;

                node->next = next;
                node->prev = prev;
                prev->next = node;
                next->prev = node;

                return;
            }
            curr = curr->next;
            idx ++;
        }
    }
    
    void deleteAtIndex(int index) {
        int idx = 0;
        Node* curr = left->next;

        while (curr != nullptr){
            if(idx == index && curr != right){
                Node* next = curr->next;
                Node* prev = curr->prev;

                prev->next = next;
                next->prev = prev;

                delete curr;
                return;
            }
            curr = curr->next;
            idx ++;
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