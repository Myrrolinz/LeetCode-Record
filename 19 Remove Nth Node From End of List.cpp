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
    // 双指针移动法
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* temp = dummyHead;
        for(int i = 0; i < n; i++) {
            // if(temp->next)
            temp = temp->next;
        }
        ListNode* curr = head;
        ListNode* prev = dummyHead;
        while(temp->next) {
            temp = temp->next;
            curr = curr->next;
            prev = prev->next;
        }
        prev->next = curr->next;
        return dummyHead->next;
    }
};