// vue.config.js
module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:7200',
                secure: true,
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
        }
    } 
}