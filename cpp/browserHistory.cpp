/*
https://leetcode.com/problems/design-browser-history/description/
*/

class Node{
    public:
        Node* next = nullptr;
        Node* prev = nullptr;
        string val;

        Node(string url){
            val = url;
        }
};

class BrowserHistory {
public:
    Node* curr = nullptr;
    Node* left = nullptr;
    Node* right = nullptr;

    BrowserHistory(string homepage) {
        left = new Node("");
        right = new Node("");
        
        curr = new Node(homepage);
        curr->prev = left;
        curr->next = right;

        left->next = curr;
        right->prev = curr;
    }
    
    void visit(string url) {
        Node* prev = curr;
        Node* next = right;   //clear forward history
        
        curr = new Node(url);
        curr->prev = prev;
        curr->next = next;

        prev->next = curr;
        next->prev = curr;
    }
    
    string back(int steps) {
        while(steps>0){
            if(curr->prev != left){
                curr = curr->prev;
                steps --;
            }
            else{
                break;
            }
        }
        return curr->val;
    }
    
    string forward(int steps) {
        while(steps>0){
            if(curr->next != right){
                curr = curr->next;
                steps --;
            }
            else{
                break;
            }
        }
        return curr->val;
    }
};
