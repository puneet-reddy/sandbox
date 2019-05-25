

// Draw a simple bar chart.
function BarChart(cxt) {
    // Private properties & methods
    var self = this;

    var SI_SYMBOL = ["", "k", "M", "G", "T", "P", "E"];

    var abbreviateNumbers = function(numbers){
        var maxNumber = numbers[0] || 0;
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

    var drawBox = function(x, y, height, width) {
        var oldStyle = cxt.strokeStyle;
        var oldWidth = cxt.lineWidth;
        cxt.strokeStyle = "black";
        cxt.lineWidth = 1;
        cxt.beginPath();
        cxt.moveTo(x, y);
        cxt.lineTo(x, y + height);
        cxt.lineTo(x + width, y + height);
        cxt.lineTo(x + width, y);
        cxt.lineTo(x, y);
        cxt.stroke();
        // Reset what we had at the start
        cxt.strokeStyle = oldStyle;
        cxt.lineWidth = oldWidth;
    }

    var draw = function(data) {
        var numOfBars = data.length;
        var barWidth;
        var barHeight;
        var border = 2;
        var ratio;
        var maxBarHeight;
        var largestValue;
        var graphAreaWidth = self.width;
        var graphAreaHeight = self.height;
        var yOffset = 0;
        var xOffset = 0;
        var i;

        // Ensure that the canvas size matches the width & height
        if (cxt.canvas.width !== self.width) {
            cxt.canvas.width = self.width;
        }
        if (cxt.canvas.height !== self.height) {
            cxt.canvas.height = self.height;
        }

        drawBox(0, 0, self.height, self.width);

        self.yAxisLabels = genAxisLabels(data);

        // Make room for the labels and legends.
        if (self.xAxisLabels.length) {
            graphAreaHeight -= 25;
            yOffset += 25;
        }
        if (self.xLegend) {
            graphAreaHeight -= 15;
            yOffset += 15;
        }
        if (self.yAxisLabels.length) {
            graphAreaWidth -= 25;
            xOffset += 25;
        }
        if (self.yLegend) {
            graphAreaWidth -= 15;
            xOffset += 15;
        }
        // Bar dimensions
        barWidth = (graphAreaWidth - xOffset) / numOfBars - self.margin * 2;
        maxBarHeight = graphAreaHeight - 25;

        // Draw the x-axis
        cxt.fillStyle = self.barColor;
        cxt.fillRect(
            self.margin + xOffset,
            graphAreaHeight,
            graphAreaWidth - self.margin * 2,
            4
        );

        // Draw the y-axis
        console.log(self.yAxisLabels);
        cxt.save();
        cxt.lineWidth = 1;
        cxt.strokeStyle = "#000000";
        cxt.beginPath();
        cxt.moveTo(self.margin + xOffset - 5, graphAreaHeight + 5);
        cxt.lineTo(self.margin + xOffset - 5, 20);
        cxt.stroke();
        ySteps = (graphAreaHeight + 5 - 20) / self.yAxisLabels.length;
        self.yAxisLabels.reverse();
        for (i = 0; i < self.yAxisLabels.length; i++) {
            cxt.beginPath();
            cxt.moveTo(self.margin + xOffset - 5, ySteps * i + 20);
            cxt.lineTo(self.margin + xOffset - 10, ySteps * i + 20);
            cxt.stroke();
            cxt.fillText(self.yAxisLabels[i], self.margin + xOffset - 25, ySteps * i + 22.5);
        }
        cxt.restore();

        // Draw the grid
        cxt.save();
        cxt.strokeStyle = self.gridColor;
        cxt.lineWidth = 1;
        ySteps = (graphAreaHeight + 5 - 20) / self.yAxisLabels.length;
        for (i = 0; i < self.yAxisLabels.length; i++) {
            cxt.beginPath();
            cxt.moveTo(self.margin + xOffset - 5, ySteps * i + 20);
            cxt.lineTo(graphAreaWidth + xOffset - self.margin, ySteps * i + 20);
            cxt.stroke();
        }
        for (i = 0; i < data.length; i++) {
            cxt.beginPath();
            cxt.moveTo(self.margin + (i * graphAreaWidth / numOfBars) + xOffset + barWidth / 2, 20);
            cxt.lineTo(self.margin + (i * graphAreaWidth / numOfBars) + xOffset + barWidth /2 , graphAreaHeight);
            cxt.stroke();
        }
        cxt.restore();

        for (i = 0; i < data.length; i++) {
            largestValue = largestValue > data[i] ? largestValue : data[i];
        }
        
        for (i = 0; i < data.length; i++) {
            if (self.maxValue) {
                ratio = data[i] / self.maxValue;
            } else {
                ratio = data[i] / largestValue
            }
            barHeight = ratio * maxBarHeight;

            // Turn on the shadows
            cxt.shadowOffsetX = 2;
            cxt.shadowOffsetY = 4;
            cxt.shadowColor = "#000032";
            cxt.shadowBlur = 5;

            // Draw the bars
            cxt.fillStyle = self.barColor;
            cxt.fillRect(
                self.margin + i * graphAreaWidth / numOfBars + xOffset,
                graphAreaHeight - barHeight,
                barWidth,
                barHeight
            );
            //Turn off shadows
            cxt.shadowOffsetX = cxt.shadowOffsetY = cxt.shadowBlur = 0;

            // Write the bar labels if they're provided
            if (self.xAxisLabels[i]) {
                cxt.fillStyle = "black";
                cxt.font = "10px Futura Book";
                cxt.textAlign = "center";
                cxt.fillText(
                    self.xAxisLabels[i],
                    xOffset + i * graphAreaWidth / numOfBars + (graphAreaWidth / numOfBars) / 2,
                    self.height - 25
                );
            }
        }
        cxt.fillStyle = "black";
        cxt.font = "10px Futura Book";
        cxt.textAlign = "center";
        cxt.fillText(self.xLegend, graphAreaWidth / 2 + xOffset, self.height - 10);
        cxt.save();
        cxt.rotate(-Math.PI / 2);
        cxt.fillText(self.yLegend, -graphAreaHeight / 2, xOffset - 25);
        cxt.restore();
    }

    //Public properties & methods
    this.width = 250;
    this.height = 150;
    this.maxValue;
    this.margin = 5;
    this.barColor = "black";
    this.backgroundColor = "#fff";
    this.gridColor = '#f0f0f0';
    this.xAxisLabels = [];
    this.yAxisLabels = [];
    this.xLegend;
    this.yLegend;

    this.update = function(data) {
        console.log(self);
        draw(data);
    }
}