
function LineGraph(cxt) {
    this.width = 450;
    this.height = 350;
    this.margin = 25;
    this.xArr = [];
    this.xLabels = [];
    this.yArr = [];
    var self = this;
    var graphHeight = self.height + 2 * self.margin;
    var graphWidth = self.width + 2 * self.margin;
    this.backgroundColor = '#fff'
    var graphTop = self.margin;
    var graphBottom = graphTop + self.height;
    var graphLeft = self.margin;
    var graphRight = graphLeft + self.width;
    var xGridResolution;
    var yGridResolution;
    var yGridSpacing;
    var xGridSpacing;
    var gridColor = "#F0F0F0";
    var gridLineWidth = 1;
    var isDebug = true 

    if (isDebug) var log = console.log.bind(window.console)
    else var log = function(){}

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

    var getGraphLimit = function (someArr) {
        log("Array input for getGraphLimit:");
        log(someArr);
        if (typeof someArr == 'undefined' || someArr.length === 0) {
            log(typeof someArr);
            log(someArr.length);
            return 0;
        }
        var maxVal = 0;
        for (var i = 0; i < someArr.length; i += 1) {
            maxVal = maxVal > someArr[i] ? maxVal : someArr[i];
        }
        log(maxVal);
        var digits = 0
        for (var startNum = maxVal; startNum > 0;) {
            startNum = Math.floor(startNum / 10);
            digits += 1;
        }
        log(digits);
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
        log("Graph Limit:");
        log(graphLimit);
        graphSteps = abbreviateNumbers(graphSteps);
        return [graphLimit, graphSteps]
    }

    var clearCanvas = function () {
        cxt.clearRect(0, 0, cxt.canvas.width, cxt.canvas.height);
    }

    var initGraph = function () {
        // Set the canvas size if changed
        if (cxt.canvas.width !== graphWidth) {
            cxt.canvas.width = graphWidth;
        }
        if (cxt.canvas.height !== graphHeight) {
            cxt.canvas.height = graphHeight;
        }

        // Draw the background
        cxt.fillStyle = self.backgroundColor;
        cxt.fillRect(0, 0, cxt.canvas.width, cxt.canvas.height);
    }

    var drawBoundingBox = function () {
        cxt.strokeStyle = 'black';
        cxt.lineWidth = 2;
        cxt.beginPath()
        cxt.moveTo(0, 0);
        cxt.lineTo(0, cxt.canvas.height);
        cxt.lineTo(cxt.canvas.width, cxt.canvas.height);
        cxt.lineTo(cxt.canvas.width, 0);
        cxt.lineTo(0, 0);
        cxt.stroke();
    }

    var drawXAxis = function (xArr) {
        xGridResolution = xGridResolution || xArr.length;

        if (self.xLabels && self.xLabels.length == xGridResolution) {
            graphBottom -= 25; //Shift the graph to make room for text
        }

        // Draw X axis
        cxt.strokeStyle = 'black';
        cxt.lineWidth = 10;
        cxt.beginPath();
        cxt.moveTo(graphRight, graphBottom);
        cxt.lineTo(graphLeft, graphBottom);
        cxt.stroke();

        // Mark the scale on the X axis
        cxt.lineWidth = 2;
        for (var i = 1; i <= xGridResolution; i +=1 ) {
            cxt.moveTo(xGridSpacing * i + self.margin, graphBottom);
            cxt.lineTo(xGridSpacing * i + self.margin, graphBottom + 10);
            cxt.stroke();
        }
        cxt.lineWidth = gridLineWidth;

        // Write the values for the X axis steps
        cxt.fillStyle = 'black';
        cxt.font = '12px futura-medium';
        cxt.textAlign = 'center';
        log(self.xLabels);
        if (typeof self.xLabels != 'undefined' && self.xLabels.length > 0) {
            for (var i = 1; i <= self.xLabels.length; i += 1) {
                cxt.fillText(
                    self.xLabels[i - 1],
                    xGridSpacing * i + self.margin,
                    graphBottom + 25
                );
            }
        }
    }

    var drawYAxis = function (yArr) {

        // Calculations & adjustments
        var yGridLimits = getGraphLimit(yArr);
        var yGridMax = yGridLimits[0];
        var yGridSteps = yGridLimits[1];
        log(yGridLimits);
        log(yGridMax);
        log(yGridSteps);
        if (typeof yGridSteps == 'undefined' || yGridSteps.length === 0) {
            yGridResolution = yGridResolution || yArr.length;
        } else {
            yGridResolution = yGridSteps.length;
            graphLeft += 25; //Making space for the text
        }

        // Draw Y axis
        cxt.strokeStyle = 'black';
        cxt.beginPath();
        cxt.lineWidth = 2;
        cxt.moveTo(graphLeft, graphBottom);
        cxt.lineTo(graphLeft, graphTop);
        cxt.stroke();
         
        // Draw marks on the Y-axis (Starting to 1 to avoid the top line)
        for (var i = 1; i < yGridResolution; i += 1) {
            cxt.moveTo(graphLeft, yGridSpacing * i + self.margin);
            cxt.lineTo(graphLeft - 5, yGridSpacing * i + self.margin);
            cxt.stroke();
        }
        cxt.lineWidth = gridLineWidth;

        // Write the values for the Y-axis steps
        cxt.fillStyle = "#000000";
        cxt.font = "12px futura-medium";
        cxt.textAlign = "center";
        if (typeof yGridSteps != 'undefined' && yGridSteps.length !== 0) {
            yGridSteps.reverse();
            for (var i = 1; i < yGridResolution; i += 1) {
                cxt.fillText(
                    yGridSteps[i],
                    graphLeft - 25,
                    yGridSpacing * i + self.margin
                );
            }
        }
    }

    var drawGridLines = function (xArr, yArr) {
        // Draw the grid lines
        log(xArr);
        log(yArr);
        cxt.lineWidth = gridLineWidth;
        yGridResolution = yGridResolution || yArr.length;
        xGridResolution = xGridResolution || xArr.length;
        cxt.strokeStyle = gridColor;
        cxt.beginPath();
        for (var i = 1; i < yGridResolution; i += 1) {
            cxt.moveTo(graphLeft, yGridSpacing * i + self.margin);
            cxt.lineTo(graphRight, yGridSpacing * i + self.margin);
            cxt.stroke();
        }
        for (var i = 1; i <= xGridResolution; i += 1) {
            cxt.moveTo(xGridSpacing * i + self.margin, graphBottom);
            cxt.lineTo(xGridSpacing * i + self.margin, graphTop);
            cxt.stroke();
        }
    }

    var drawGraph = function(dataArr) {
        var arrLen = dataArr.length;

        var maxValue = 0;
        for (var i = 0;  i < arrLen; i += 1) {
            maxValue = maxValue > dataArr[i] ? maxValue : dataArr[i];
        }
        var ratio = maxValue / self.height;

        cxt.beginPath();
        cxt.lineJoin = 'round';
        cxt.strokeStyle = '#ff9702';
        cxt.moveTo(self.margin + xGridSpacing, graphHeight - self.margin - (dataArr[0] / ratio));
        for ( var i = 1; i < arrLen; i += 1) {
            cxt.lineTo(xGridSpacing * (i + 1) + self.margin, graphHeight - self.margin - (dataArr[i] / ratio));
            cxt.stroke();
        }
        cxt.shadowColor = '#000032';
        cxt.shadowOffsetX = -3;
        cxt.shadowOffsetY = 7;
        cxt.shadowBlur = 5;
        cxt.stroke();
    }

    var draw = function (xArr, yArr) {
        clearCanvas();
        initGraph();
        drawYAxis(xArr);
        drawXAxis(xArr);
        drawBoundingBox();
        drawGridLines(xArr, yArr);
        drawGraph(xArr);
    }

    this.update = function () {
        if (typeof self.xArr == 'undefined' || self.xArr.length === 0) {
            console.log('Warning: No x-axis array (xArr) provided');
        }
        if (typeof self.yArr == 'undefined' || self.yArr.length === 0) {
            console.log('Warning: No y-axis array (yArr) provided');
        }
        xGridResolution = self.xArr.length || 10;
        yGridResolution = self.yArr.length || 12;
        yGridSpacing = self.height / yGridResolution;
        xGridSpacing = self.width / xGridResolution;
        draw(self.xArr, self.yArr);
    }
};