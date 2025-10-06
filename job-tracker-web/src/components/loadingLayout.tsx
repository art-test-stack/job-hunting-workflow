import { LoadingOverlay } from "@mantine/core";


export default function LoadingLayout () {
    const componentSize = 100; // Replace with the actual size of the component
    return <LoadingOverlay visible={true} zIndex={componentSize / 2} />
}