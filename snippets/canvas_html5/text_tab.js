
// Draw a text tab
function TextTab(cxt) {
    //Private variables & methods
    var self = this;

    var draw = function() {
        //Reset the canvas size as required
        if (cxt.canvas.height !== self.height) {
            cxt.canvas.height = self.height;
        }
        if (cxt.canvas.width !== self.width) {
            cxt.canvas.width = self.width;
        }

        //Clear the canvas
        cxt.clearRect(0, 0, cxt.canvas.width, cxt.canvas.height);

        //Draw the background
        cxt.save();
        cxt.fillStyle = self.backgroundColor;
        cxt.fillRect(0, 0, cxt.canvas.width, cxt.canvas.height);
        cxt.restore();

        //Draw the text
        cxt.save();
        cxt.fillStyle = self.textColor;
        cxt.font = self.textFont;
        cxt.textAlign = "center";
        cxt.fillText(
            self.textContent,
            self.width * 0.5,
            self.height * 0.75
        )
        cxt.font = self.legendFont;
        cxt.fillText(
            self.textLegend,
            self.width * 0.5,
            self.height * 0.85
        )
    }

    this.width = 50;
    this.height = 200;
    this.textContent = 'Sample';
    this.textLegend = 'Testing 123';
    this.textFont = 'bold 18px futura-medium';
    this.legendFont = '10px futura-medium';

    this.update = function() {
        draw();
    }
}