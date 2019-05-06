
// A javascript implementation of the common snake game

function SnakeGrid(cxt) {
    var self = this; // Capturing the component context
    var spawned = false;
    var xMax;
    var xMin;
    var yMax;
    var yMin;

    var resize = function () {
        // Check and resize the canvas if required
        console.log('Resizing canvas to: ', self.height, self.width);
        if (self.height !== cxt.canvas.height) {
            cxt.canvas.height = self.height;
        }
        if (self.width !== cxt.canvas.width) {
            cxt.canvas.width = self.width;
        }
    }

    var drawBox = function (x, y, width, height) {
        // Draws a box with the bottom left corner at (x, y)
        cxt.save();
        cxt.lineWidth = 1;
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

    var drawGrid = function (x, y, width, height) {
        cxt.save();
        cxt.lineWidth = 0.1;
        cxt.strokeStyle = '#DDDDDD';
        var xCells = width / self.cellSize;
        console.log(xCells);
        for (var i = 0; i <= xCells; i++) {
            cxt.moveTo(x + i * self.cellSize, y);
            cxt.lineTo(x + i * self.cellSize, y + height);
            cxt.stroke();
        }
        var yCells = height / self.cellSize;
        for (var j = 0; j <= yCells; j++) {
            cxt.moveTo(x, y + j * self.cellSize);
            cxt.lineTo(x + width, y + j * self.cellSize);
            cxt.stroke();
        }
        cxt.restore();

        // Initialize the boundaries.
        xMin = 0;
        xMax = xCells;
        yMin = 0;
        yMax = yCells;

        // Initialize cells array.
        self.cells = Array(xCells).fill(0).map(x => Array(yCells).fill(0))
        console.log('Cells initialized to: ', self.cells);
    }

    var fillCell = function (cell, color) {
        // Fills the cell at x column, y row with the given color
        cxt.save();
        cxt.fillStyle = color;
        cxt.fillRect(
            self.margins + self.cellSize * cell[0],
            self.margins + self.cellSize * cell[1],
            self.cellSize, self.cellSize);
        cxt.restore();
        self.cells[cell[0]][cell[1]] = 1;
    }

    var spawnSnake = function () {
        self.snake.push([0, 0]);
        self.snake.push([0, 1]);
        fillCell([0, 0], '#000000');
        fillCell([0, 1], '#000000');
        spawned = true;
    }


    var spawnFood = function () {
        while (true) {
            var xLocation = Math.floor(Math.random() * self.cells[0].length - 1);
            var yLocation = Math.floor(Math.random() * self.cells.length - 1);
            if (self.cells[xLocation][yLocation] !== 1) {                
                fillCell([xLocation, yLocation], '#00FFFF');
                self.cells[xLocation][yLocation] = 2;
                console.log('Food spawned at: ', xLocation, yLocation);
                break;
            }
        }
    }


    var move = function () {
        if (!spawned) {
            console.log('Can\'t move a snake which hasn\'t spawned');
            return
        }
        head = self.snake[self.snake.length - 1];
        tail = self.snake[0];
        var newHead = [head[0] + self.direction[0], head[1] + self.direction[1]];
        // Check for colissions
        console.log('xMax, xMin, yMax, yMin: ', xMax, xMin, yMax, yMin);
        if (newHead[0] > xMax | newHead[0] < xMin | newHead[1] > yMax | newHead[1] < yMin | self.cells[newHead[0]][newHead[1]] === 1) {
            window.alert('Game over. The snake is dead!');
            clearInterval(self.gameLoop);
            return;
        }
        if (self.cells[newHead[0]][newHead[1]] !== 2) {
            fillCell(tail, '#FFFFFF');
            self.snake.shift();
            self.cells[tail[0]][tail[1]] = 0;
        } else {
            spawnFood();
        }
        fillCell(newHead, '#000000');
        self.cells[head[0] + self.direction[0]][head[1] + self.direction[1]] = 1;
        self.snake.push(newHead);
    }

    this.lineWidth = 1;
    this.margins = Math.min(25, window.innerWidth / 10);
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.cellSize = 10; // Size of each cell in pixels.
    this.cells = [];
    this.direction = [0, 1];
    this.snake = [];
    this.gameLoop;

    this.update = function () {
        resize();
        drawBox(
            this.margins, // x
            this.margins, // y
            cxt.canvas.width - 2 * this.margins, // width
            cxt.canvas.height - 2 * this.margins // height
        );
        drawGrid(
            this.margins,
            this.margins,
            cxt.canvas.width - 2 * this.margins,
            cxt.canvas.height - 2 * this.margins
        );
        console.log(
            'Grid Dimensions: ',
            this.margins, // x
            this.margins, // y
            cxt.canvas.width - 2 * this.margins, // width
            cxt.canvas.height - 2 * this.margins // height
        );
        spawnSnake();
        spawnFood();
    }

    this.keydownHandler = function (e) {
        if (!e) e = window.event;
        switch (e.keyCode) {
            case 37:
                self.direction = [-1, 0];
                break;
            case 38:
                self.direction = [0, -1];
                break;
            case 39:
                self.direction = [1, 0];
                break;
            case 40:
                self.direction = [0, 1]
                break;
        }
    }

    this.start = function () {
        self.gameLoop = setInterval(move, 80);
    }
}