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
  
    print() {
      if (this.width > 0 && this.height > 0) {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      }
    }
  }
  
  module.exports = Rectangle;
  