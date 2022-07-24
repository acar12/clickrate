import { Container, Heading, Input, InputGroup, InputRightElement, Button, Progress } from "@chakra-ui/react"

const App = () => {
    return (
        <Container>
            <Heading mt={12} mb={8}>Clickrate</Heading>
            <InputGroup size="md">
                <Input pr="4.5rem" placeholder="Text"/>
                <InputRightElement width="4.5rem">
                    <Button h="1.75rem" size="sm">Get %</Button>
                </InputRightElement>
            </InputGroup>
            <Progress  mt={6} value={50} isIndeterminate={true}/>
        </Container>
    )
}

export default App
