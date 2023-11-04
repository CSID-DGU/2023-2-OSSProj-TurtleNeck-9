const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
  mode: 'development',
  entry: {
    main: './src/index.tsx'
  },
  devtool: 'inline-source-map',
  output: {
    path: path.resolve(__dirname, 'dist')
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.jsx', '.js']
  },
  module: {
    rules: [
      {
        test: /\.(tsx|ts|jsx|js)$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      // 1.import 가능 -> 2.모듈이 실행될 때 html 파일의 <head>에 문자열화 된 CSS가 <style>태그로 삽입
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './index.html'
    })

  ]
}