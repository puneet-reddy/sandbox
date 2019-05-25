
var SI_SYMBOL = ["", "k", "M", "G", "T", "P", "E"];

function abbreviateNumbers(numbers){
    maxNumber = numbers[0] || 0;
    for (var i = 0; i < numbers.length; i += 1) {
        maxNumber = maxNumber > numbers[i] ? maxNumber : numbers[i];
    }
    var isNegative = maxNumber < 0;

    maxNumber = isNegative ? maxNumber * -1 : maxNumber;

    // what tier? (determines SI symbol)
    var tier = Math.log10(maxNumber) / 3 | 0;

    if(tier == 0) return numbers;

    // get suffix and determine scale
    var suffix = SI_SYMBOL[tier];
    var scale = Math.pow(10, tier * 3);

    // scale the number
    for (var i = 0; i < numbers.length; i += 1) {
        var scaled = numbers[i] / scale;
        scaled = isNegative ? scaled * -1 : scaled;
        numbers[i] = scaled.toFixed(1) + suffix;
    }
    return numbers;
}

var genAxisLabels = function (someArr) {
    // Returns a list of values for the axis labels.
    if (typeof someArr == 'undefined' || someArr.length === 0) {
        return 0;
    }
    var maxVal = 0;
    for (var i = 0; i < someArr.length; i += 1) {
        maxVal = maxVal > someArr[i] ? maxVal : someArr[i];
    }
    var digits = 0
    for (var startNum = maxVal; startNum > 0;) {
        startNum = Math.floor(startNum / 10);
        digits += 1;
    }
    var graphLimit = 0;
    var graphSteps = [];
    while (graphLimit < maxVal) {
        graphLimit += 10 ** (digits - 1);
        graphSteps.push(graphLimit);
    }
    // To avoid too coarse a grain for the axis scale.
    if (graphSteps.length < 5) {
        graphLimit = 0
        graphSteps = []
        while (graphLimit < maxVal) {
            graphLimit += 10 ** (digits - 2);
            graphSteps.push(graphLimit);
        }
    }
    graphSteps = abbreviateNumbers(graphSteps);
    return graphSteps
}

export default genAxisLabels;