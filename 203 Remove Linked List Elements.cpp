/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr) return nullptr;
        ListNode* curr = head;
        // 删除头结点情况
        while(head->val == val) {
            if(head->next)
                head = head->next;
            else
                return nullptr;
        }
        while(curr->next) {
            if(curr->next->val == val) {
                ListNode* tmp = curr->next;
                curr->next = tmp->next;
                delete tmp;
            } else {
                curr = curr->next;
            }
        }
        return head;
    }
};