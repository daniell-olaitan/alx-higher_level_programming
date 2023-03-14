#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; ++i) {
      for (let j = 0; j < this.width; ++j) {
        process.stdout.write(c);
      }

      console.log('');
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
