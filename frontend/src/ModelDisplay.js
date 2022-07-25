import { Input, InputGroup, InputRightElement, Button, Progress, Flex, Box, Spacer } from "@chakra-ui/react"
import { useState } from "react"
import axios from "axios"

const baseURL = window.location.origin

const ModelDisplay = () => {
    const [text, setText] = useState("")
    const [value, setValue] = useState(-1) // -1 is magic number, means no data provided

    const getPredictedValue = () => {
        axios.get(`${baseURL}/text/${text}`).then((response) => {
            setValue(-1)
            const percent = Math.floor(response.data["percent_clickbait"] * 100)
            setValue(percent)
        })
    }

    return (
        <>
            <InputGroup size="md">
                <Input value={text} onChange={(e) => setText(e.target.value)} pr="4.5rem" placeholder="Text"/>
                <InputRightElement width="4.5rem">
                    <Button h="1.75rem" size="sm" onClick={getPredictedValue}>Get %</Button>
                </InputRightElement>
            </InputGroup>
            <Progress  mt={6} value={value} isIndeterminate={value == -1 ? true : false}/>
            <Flex>
                <Box p={2} pl={0}>Not Clickbait</Box>
                <Spacer/>
                <Box p={2} pl={0}>{value == -1 ? "Not Calculated" : `${value}%`}</Box>
                <Spacer/>
                <Box p={2} pr={0}>Clickbait</Box>
            </Flex>
        </>
    )
}

export default ModelDisplay
