void moveZeroes(vector<int> &nums)
{
    vector<int> ans;
    int j = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] != 0)
        {
            ans.push_back(nums[i]);
            j++;
        }
    }
    for (int i = 0; i < nums.size() - j; i++)
    {
        ans.push_back(0);
    }
    nums = ans;
}