/*
Given an array find its (i,j) segment sum
For k queries takes O(Nk)
But make a prefix array in O(N) then do it on O(1) for each query so O(N+k)
Works for static arrays only that would not change in future
*/

#include <iostream>
#include <vector>

int prefixQuery(std::vector<int> prefixSum, int left, int right)
{
    int sum = prefixSum[right];
    if (left != 0)
    {
        sum -= prefixSum[left-1];
    }
    return sum;
}

int main()
{
    const int N = 10;
    std::vector<int> arr({1,2,3,4,5,6,7,8,9,10});
    std::vector<int> prefixSum(N,0);

    //Prefix sum construction;
    //prefixSum[i] = sum of array from 0 to ith position (inclusive both)
    prefixSum[0] = arr[0];
    for (int i = 1; i < N; ++i)
    {
        prefixSum[i] = prefixSum[i-1]+arr[i];
    }

    for (int i = 0; i < N; ++i)
    {
        std::cout << prefixSum[i] << " ";
    }
    std::cout << std::endl;

    std::cout << prefixQuery(prefixSum, 0,6) << std::endl;
    std::cout << prefixQuery(prefixSum, 1,6) << std::endl;
}

//The addition operation can be generalized to any associative operator