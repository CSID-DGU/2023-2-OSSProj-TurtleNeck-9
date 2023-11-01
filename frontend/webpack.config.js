const path = require('path');

module.exports = {
  entry: {
    main: './src/index.jsx'
  },
  output: {
    path: path.resolve(__dirname, 'dist')
  },
  module: {
    rules: [
      {
        test: /\.(jsx|js)$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      }
    ]
  }
}