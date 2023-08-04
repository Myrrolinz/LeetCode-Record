class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        ListNode *temp;
        ListNode *prev = nullptr;
        // if(head == nullptr)
        //     return nullptr;
        // if(head->next == nullptr)
        //     return head;
        while(curr) {
            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
            // if(temp->next)
            //     temp = temp->next;
        }
        return prev;
    }
};