import React from "react"
import ReactDOM from "react-dom"
import { ChakraProvider } from "@chakra-ui/react"
import App from "./App.js"

const root = ReactDOM.createRoot(document.getElementById("root"))
root.render(<ChakraProvider><App/></ChakraProvider>, root)
