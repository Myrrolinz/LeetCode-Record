class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int num = 1;
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        for(int cnt = 0; cnt < n - 1; cnt++) {
            for (int i = cnt; i < n - cnt - 1; i++)
                matrix[cnt][i] = num++;
            for (int j = cnt; j < n - cnt - 1; j++)
                matrix[j][n - 1 - cnt] = num++;
            for (int x = n - cnt - 1; x > cnt; x--)
                matrix[n - 1 - cnt][x] = num++;
            for (int y = n - cnt - 1; y > cnt; y--)
                matrix[y][cnt] = num++;
        }
        // 奇数时，需要单独赋值
        if (n % 2) {
            matrix[n/2][n/2] = num;
        }
        return matrix;
    }
};