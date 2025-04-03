module.exports = {
  "presets": [
    ["@babel/preset-env", {
      "modules": "commonjs"  // <--- importante para eliminar `import/export`
    }],
    "@babel/preset-react"
  ],
  "plugins": [
    "@babel/plugin-transform-runtime",
    "@babel/plugin-proposal-class-properties",
    "@babel/plugin-proposal-object-rest-spread"
  ]
}
