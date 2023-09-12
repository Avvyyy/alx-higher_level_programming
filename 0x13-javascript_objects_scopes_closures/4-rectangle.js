class Rectangle {
    constructor(w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        this.width = 0;
        this.height = 0;
      }
    }
  
    // Methos to print a rectangle
    print() {
      if (this.width > 0 && this.height > 0) {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      }
    }

    // Method to rotate a rectangle by switching its width and height
    rotate () {
        let temp = this.width;
        this.width = this.height;
        this.height = temp;
    }

    // Method that doubles the width and height of a rectangle
    double () {
        this.width *= 2;
        this.height *= 2;
    }

  }
  
  module.exports = Rectangle;
  