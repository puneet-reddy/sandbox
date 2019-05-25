
function BarGraph(cxt) {
    // Private properties and methods
    var that = this;
    var startArr;
    var endArr;
    var looping = false;

    // Loop method to adjust height and redraw (if required)
    var loop = function () {
        var delta;
        var animationComplete = true;

        // Prevent update while already looping.
        looping = true;

        for (var i = 0; i < endArr.length; i += 1) {
            delta = (endArr[i] - startArr[i]) / that.animationSteps;
            that.curArr[i] += delta;
            if (delta) {
                animationComplete = false;
            }
        };
        if (animationComplete) {
            looping = false;
        } else {
            draw(that.curArr);
            setTimeout(loop, that.animationInterval / that.animationSteps);
        };
    };

    // Draw method to update the canvas with the current display
    var draw = function (arr) {
        var numOfBars = arr.length;
        var barWdith;
        var barHeight;
        var border = 2;
        var ratio;
        var maxBarHeight;
        var gradient;
        var largestValue;
        var graphAreaX = 0;
        var graphAreaY = 0;
        var graphAreaWidth = that.width;
        var graphAreaHeight = that.height;
        var i;

        // Update the dimentions only if they have changed
        if (cxt.canvas.width !== that.width || cxt.canvas.height !== that.height) {
            cxt.canvas.width = that.width;
            cxt.canvas.height = that.height;
        };

        // Draw the background
        cxt.fillStyle = that.backgroundColor;
        cxt.fillRect(0, 0, that.width, that.height);

        // Make room for labels (if they exist)
        if (that.xAxisLabelArr.length) {
            graphAreaHeight -= 40;
        };

        // Bar dimensions calculation
        barWdith = graphAreaWidth / numOfBars - that.margin * 2;
        maxBarHeight = graphAreaHeight - 25;

        var largestValue = 0;
        for (i = 0; i < arr.length; i += 1) {
            if (arr[i] > largestValue) {
                largestValue = arr[i];
            }
        };

        // For each bar
        for (i = 0; i < arr.length; i += 1) {
            if (that.maxValue) {
                ratio = arr[i] / that.maxValue;
            } else {
                ratio = arr[i] / largestValue;
            }
            barHeight = ratio * maxBarHeight;

            // Turn on shadow
            cxt.shadowOffsetX = 2;
            cxt.shadowOffsetY = 2;
            cxt.shadowBlur = 2;
            cxt.shadowColor = "#999";

            // Draw bar background
            cxt.fillStyle = "#333";
            cxt.fillRect(
                that.margin + i * that.width / numOfBars,
                graphAreaHeight - barHeight,
                barWdith,
                barHeight);

            // Turn off shadows
            cxt.shadowOffsetX = cxt.shadowOffsetY = cxt.shadowBlur = 0;

            // Create gradient
            gradient = cxt.createLinearGradient(0, 0, 0, graphAreaHeight);
            gradient.addColorStop(1 - ratio, that.colors[i % that.colors.length]);
            gradient.addColorStop(1, "#ffffff");
            cxt.fillStyle = gradient;
            cxt.fillRect(
                that.margin + i * that.width / numOfBars + border,
                graphAreaHeight - barHeight + border,
                barWdith - border * 2,
                barHeight - border * 2
            );

            // Write bar value
            cxt.fillStyle = "#333";
            cxt.font = "bold 12px sans-serif";
            cxt.textAlign = "center";
            cxt.fillText(
                parseInt(arr[i], 10),
                i * that.width / numOfBars + (that.width / numOfBars) / 2,
                graphAreaHeight - barHeight - 10
            );

            // Draw bar label if it exists
            if (that.xAxisLabelArr[i]) {
                cxt.fillStyle = "#333";
                cxt.font = "bold 12px sans-serif";
                cxt.textAlign = "center";
                cxt.fillText(
                    that.xAxisLabelArr[i],
                    i * that.width / numOfBars + (that.width / numOfBars) / 2,
                    that.height - 10
                );
            }
        }
    };

    // Public properties and methods
    this.width = 300;
    this.height = 150;
    this.maxValue;
    this.margin = 5;
    this.colors = ["purple", "red", "green", "yellow"];
    this.curArr = [];
    this.backgroundColor = "#fff";
    this.xAxisLabelArr = [];
    this.yAxisLabelArr = [];
    this.animationInterval = 100;
    this.animationSteps = 10;

    // Update method sets the end bar array and starts the animation
    this.update = function (newArr) {
        console.log(that.curArr);
        console.log(that.startArr);
        console.log(that.endArr);
        console.log(newArr);
        if (that.curArr.length !== newArr.length) {
            that.curArr = newArr;
            draw(newArr);
        } else {
            startArr = that.curArr;
            endArr = newArr;
            if (!looping) {
                loop();
            }
        }
    };

    this.animate = function() {
        if (that.curArr) {
            var newArr = [];
            for (var i = 0; i < that.curArr.length; i += 1) {
                newArr[i] = Math.floor((Math.random() * 10) + 1);
            }
            that.update(newArr);
            setTimeout(that.animate, that.animationInterval * 20);
        }
    }
}