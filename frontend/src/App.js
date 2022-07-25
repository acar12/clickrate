import { Container, Heading } from "@chakra-ui/react"
import ModelDisplay from "./ModelDisplay.js"

const App = () => {
    return (
        <Container>
            <Heading mt={12} mb={8}>Clickrate</Heading>
            <ModelDisplay/>
        </Container>
    )
}

export default App
