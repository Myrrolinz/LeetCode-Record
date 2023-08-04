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
    ListNode* swapPairs(ListNode* head) {
        // 使用虚拟节点，更具有一般性
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* curr = dummyHead;
        while(curr->next && curr->next->next) {
            ListNode* temp1 = curr->next->next->next;
            ListNode* temp2 = curr->next;
            curr->next = curr->next->next;
            curr->next->next = temp2;
            temp2->next = temp1;
            curr = curr->next->next;
        }
        return dummyHead->next;
    }
};