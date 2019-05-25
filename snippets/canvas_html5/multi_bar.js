
function MultiBar(cxt) {
    //Private variables & methods
    var self = this;
    var legendMargin;
    var yLegendMargin;
    var xLegendMargin;
    var yLabelMargin;
    var xLabelMargin;
    var xAxisWidth = 4;
    var graphTop = 0;
    var graphLeft = 0;
    var graphHeight;
    var graphWidth;

    var SI_SYMBOL = ["", "k", "M", "G", "T", "P", "E"];

    var abbreviateNumbers = function (numbers) {
        var maxNumber = numbers[0] || 0;
        for (var i = 0; i < numbers.length; i += 1) {
            maxNumber = maxNumber > numbers[i] ? maxNumber : numbers[i];
        }
        var isNegative = maxNumber < 0;

        maxNumber = isNegative ? maxNumber * -1 : maxNumber;

        // what tier? (determines SI symbol)
        var tier = Math.log10(maxNumber) / 3 | 0;

        if (tier == 0) return numbers;

        // get suffix and determine scale
        var suffix = SI_SYMBOL[tier];
        var scale = Math.pow(10, tier * 3);

        // scale the number
        for (var i = 0; i < numbers.length; i += 1) {
            var scaled = numbers[i] / scale;
            scaled = isNegative ? scaled * -1 : scaled;
            numbers[i] = scaled.toFixed(0) + suffix;
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
            for (var j = 0; j < someArr[i].length; j += 1) {
                maxVal = maxVal > someArr[i][j] ? maxVal : someArr[i][j];
            }
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

    var isValidData = function (data) {
        if (!Array.isArray(data) || data.length === 0) {
            console.error("No data provided!");
            return false;
        }
        if (!Array.isArray(self.xAxisLabels) || self.xAxisLabels.length === 0) {
            console.error("xAxisLabels is must be provided!");
            return false;
        };
        if (!Array.isArray(self.legends) || self.legends.length === 0) {
            console.error("legends must be provided!");
            return false;
        }
        if (!Array.isArray(self.barColors) || self.barColors.length === 0) {
            console.error("barColors must be provided!");
            return false;
        }
        if (data.length !== self.xAxisLabels.length) {
            console.error("data points don't match number of labels");
            return false;
        }
        var barCount = data[0].length;
        for (idx in data) {
            if (barCount !== data[idx].length) {
                console.error("data length mismatch in sub-array!");
                return false;
            }
        }
        if (barCount !== self.legends.length) {
            console.error("legends and bar count mismatch!");
            return false;
        }
        return true;
    }

    var resize = function () {
        // Check and resize the canvas accordingly.
        if (self.height !== cxt.canvas.height) {
            cxt.canvas.height = self.height;
        }
        if (self.width !== cxt.canvas.width) {
            cxt.canvas.width = self.width;
        }
    }

    var calculateMargins = function () {
        // Calculate the required margins and update global variables to match
        graphLeft += 20; // Y label is always present
        graphHeight -= 4; // Making space for the x-axis
        if (self.margins) {
            graphHeight -= 2 * self.margins;
            graphWidth -= 2 * self.margins;
            graphLeft += self.margins;
            graphTop += self.margins;
        }
        if (self.xLegend) {
            xLegendMargin += 20;
            graphHeight -= 20;
        }
        if (self.xAxisLabels) {
            xLabelMargin += 20;
            graphHeight -= 20;
        }
        if (self.yLegend) {
            yLegendMargin += 20;
            graphLeft += 20;
        }
        if (self.label) {
            graphTop += 20;
        }
        if (self.legends) {
            graphTop += 20;
        }
    }

    var drawBoundingBox = function (x = 0, y = 0, width, height) {
        cxt.save();
        cxt.strokeStyle = "black";
        cxt.lineWidth = 1;
        cxt.beginPath();
        cxt.moveTo(x, y);
        cxt.lineTo(width, y);
        cxt.lineTo(width, height);
        cxt.lineTo(x, height);
        cxt.lineTo(x, y);
        cxt.stroke();
        cxt.restore();
    }

    var drawXAxis = function (data) {
        var parts = data.length;
        var partLength = ((graphWidth - graphLeft) / parts) - 1;
        cxt.save();
        for (var i = 0; i < parts; i++) {
            cxt.fillStyle = "black";
            cxt.fillRect(
                graphLeft + (partLength + 1) * i,
                graphHeight - 4,
                partLength,
                4)
        }
        for (var i = 1; i < parts; i++) {
            cxt.fillStyle = "#000000";
            cxt.fillRect(
                graphLeft + (partLength + 1) * i,
                graphHeight,
                -1,
                5)
            //Draw grid lines
            cxt.fillStyle = "#F0F0F0";
            cxt.fillRect(
                graphLeft + (partLength + 1) * i,
                graphTop,
                -1,
                graphHeight - 45
            );
        }
        cxt.fillStyle = 'black';
        cxt.textAlign = "center";
        cxt.font = "10px Futura Book";
        for (var i = 0; i < self.xAxisLabels.length; i++) {
            cxt.fillText(
                self.xAxisLabels[i],
                (graphLeft + (partLength + 1) * (i + 0.5)),
                graphHeight + 10
            )
        }
        cxt.fillText(self.xLegend, 20 + (graphWidth) / 2, graphHeight + 30);
        cxt.restore();
    }

    var drawYAxis = function (data) {
        cxt.save();

        var axisValues = genAxisLabels(data);
        var tickCount = axisValues.length;
        var ySteps = (graphHeight - graphTop - self.margins) / tickCount;
        console.log(axisValues);

        //Draw grid lines
        cxt.strokeStyle = "#F0F0F0";
        for (var i = 1; i <= tickCount; i++) {
            var yPosition = graphHeight - ySteps * i;
            cxt.moveTo(graphLeft, yPosition);
            cxt.lineTo(graphWidth, yPosition);
            cxt.stroke();
        }

        cxt.strokeStyle = 'black';
        cxt.beginPath();
        cxt.lineWidth = 1;
        cxt.moveTo(graphLeft - 5, graphHeight);
        cxt.lineTo(graphLeft - 5, graphTop);
        cxt.stroke();

        //Draw graph steps
        cxt.font = '10px futura-medium';
        cxt.textAlign = 'center';
        for (var i = 1; i <= tickCount; i++) {
            var yPosition = graphHeight - ySteps * i;
            cxt.moveTo(graphLeft - 5, yPosition);
            cxt.lineTo(graphLeft - 10, yPosition);
            cxt.stroke();
            //Axis labels
            cxt.fillText(axisValues[i - 1], graphLeft - 18, yPosition + 4);
        }

        // Write the legend text
        cxt.fillStyle = 'black';
        cxt.font = '10px futura-book';
        cxt.textAlign = 'center';
        cxt.rotate(-Math.PI / 2);
        cxt.fillText(self.yLegend, -(graphHeight + graphTop) / 2, graphLeft - 30);
        cxt.restore();
    }

    var drawBars = function (data) {
        var maxVal = 0;
        for (row in data) {
            for (item in data[row]) {
                maxVal = maxVal > data[row][item] ? maxVal : data[row][item];
            }
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
            }
        }

        // This only works since we did validation
        var totalBars = data.length * data[0].length;
        var barSpacing = (graphWidth - graphLeft) / totalBars;

        cxt.save();
        //Turn on shadows
        cxt.shadowOffsetX = 2;
        cxt.shadowOffsetY = 0;
        cxt.shadowBlur = 2;
        cxt.shadowColor = "#999";
        var scaleFactor = (graphHeight - graphTop) / graphLimit;
        var counter = 0;
        for (row in data) {
            console.log(data[row]);
            for (item in data[row]) {
                console.log(data[row][item], row, item);
                cxt.fillStyle = self.barColors[item];
                cxt.fillRect(
                    graphLeft + counter * barSpacing,
                    graphHeight - data[row][item] * scaleFactor,
                    self.barWidth,
                    data[row][item] * scaleFactor - 4
                );
                counter += 1;
            }
        }
        cxt.restore();
    }

    var drawLegends = function() {
        cxt.save();
        var legendCount = self.legends.length;
        var legendWidth = (graphWidth - graphLeft) / legendCount;
        cxt.textAlign = "left";
        for(i in self.legends) {
            cxt.beginPath();
            cxt.arc(
                graphWidth - graphLeft - legendWidth * i, 
                graphTop - 10, 
                3, //Radius
                0, 
                2 * Math.PI, 
                true);
            cxt.fillStyle = self.barColors[i];
            cxt.fill();
            cxt.lineWidth = 0.1;
            cxt.stroke();
        }
        cxt.strokeStyle = 'black';
        cxt.fillStyle = 'black';
        cxt.font = "10px futura-medium";
        for (i in self.legends) {
            cxt.fillText(
                self.legends[i], 
                graphWidth - graphLeft - legendWidth * i + 5, 
                graphTop - 7);
            cxt.stroke();
        }
        cxt.restore();
    }

    var drawTitle = function() {
        cxt.save();
        cxt.strokeStyle = 'black';
        cxt.textAlign = 'left';
        cxt.font = "12px futura-medium";
        cxt.fillText(
            self.label,
            graphLeft,
            graphTop - 25
        );
        cxt.restore();
    }

    //Public variables & methods
    this.barWidth = "5px";
    this.barAlignment = "left";
    this.width;
    this.height;
    this.xLegend;
    this.yLegend;
    this.legends;
    this.xAxisLabels;
    this.barColors;
    this.margins;

    this.update = function (data) {
        // Validation
        if (!isValidData(data)) { return; }
        graphWidth = self.width;
        graphHeight = self.height;
        resize();
        drawBoundingBox(0, 0, self.width, self.height);
        calculateMargins();
        //drawBoundingBox(graphLeft, graphTop, graphWidth, graphHeight);
        drawXAxis(data);
        drawYAxis(data);
        drawBars(data);
        drawLegends();
        drawTitle();
    }
}