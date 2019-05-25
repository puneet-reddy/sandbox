
// Testing font size based on canvas size
function FontSizeTest(cxt){
    var self = this;
    
    var resize = function() {
        if(self.height !== cxt.canvas.height) {
            cxt.canvas.height = self.height;
        }
        if(self.width !== cxt.canvas.width) {
            cxt.canvas.width = self.width;
        }
    }

    var drawBox = function(x, y, width, height) {
        cxt.save();
        cxt.strokeStyle = 'black';
        cxt.beginPath();
        cxt.moveTo(x, y);
        cxt.lineTo(x, y + height);
        cxt.lineTo(x + width, y + height);
        cxt.lineTo(x + width, y);
        cxt.lineTo(x, y);
        cxt.stroke();
        cxt.restore();
    }

    var writeText = function(text) {
        cxt.save();
        cxt.font = self.font;
        cxt.textAlign = self.textAlign;
        cxt.fillText(text, self.width / 2, self.height / 2);
        cxt.stroke();
        cxt.restore();
    }

    this.height = 200;
    this.width = 200;
    this.font = '10px futura-medium';
    this.textAlign = "center";

    this.update = function(data){
        resize();
        drawBox(0, 0, self.width, self.height);
        writeText(data);
    }
}