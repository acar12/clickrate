const path = require("path")
const Plugin = require('html-webpack-plugin')

module.exports = {
    entry: path.join(__dirname, "src", "index.js"),
    output: {
        path: path.resolve(__dirname, "build")
    },
    module: {
        rules: [{
            test: /\.?js$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader",
                options: {
                    presets: [
                        '@babel/preset-env', 
                        ["@babel/preset-react", {"runtime": "automatic"}]
                    ]
                }
            }
        }]
    },
    plugins: [
        new Plugin({
            template: path.join(__dirname, "public", "index.html")
        })
    ]
}
