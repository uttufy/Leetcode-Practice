/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var dict = {}
    for(var i=0; i<nums.length; i++){
        dict[nums[i]] = i;
    }

    for(var i=0; i<nums.length; i++){
        var diff = target - nums[i];
        if(diff in dict && dict[diff]!==i){
            return [i, dict[diff]];
        }
    }

    return [];
};