function findLargest(numbers) {
    var max = numbers[0];
    numbers.forEach(function(value){
        max=(max>value)?max:value;
    });
    return max;
}
