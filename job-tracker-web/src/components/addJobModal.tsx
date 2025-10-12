import { Button, Modal, Select, TagsInput, TextInput } from "@mantine/core";
import { useForm } from '@mantine/form';
import { useDisclosure } from "@mantine/hooks";
import { DatePickerInput } from '@mantine/dates';
import { useState } from "react";
import { JobStatus } from "@/pages/jobs";

export interface AddJobModalProps {
    opened: any,
    onClose: any,
    content: any,
    onSubmit: any
    // submitNewJob: CallableFunction
}

export default function AddJobModal(props: AddJobModalProps) {
    const form = props.content
    const [dateValue, setDateValue] = useState<string | null>(form.values.application_date);

    const handleDateChange = (value: string | null) => {
        setDateValue(value);
        form.setFieldValue('applied_at', value);
    };
    const checkJobForm = () => {
        if (!form.values.title) {
            form.setFieldError('title', "Job title should be included");
            return false;
        }
        if (!form.values.company) {
            form.setFieldError('company', "Job company should be included");
            return false;
        }
        if (!form.values.location) {
            form.setFieldError('location', "Job location should be included");
            return false;
        }
        if (!form.values.status) {
            form.setFieldError('status', "Job status should be included");
            return false;
        }
        return true

    }
    const submitNewJob = () => {
        if (checkJobForm()) {
            props.onSubmit()
        }
    }
    return (
    <Modal opened={props.opened} onClose={props.onClose}>
        <TextInput
            label="Title"
            placeholder="Title"
            key={form.key('title')}
            withAsterisk
            {...form.getInputProps('title')}
        />
        <TextInput
            mt="md"
            label="Company"
            placeholder="Company"
            key={form.key('company')}
            withAsterisk
            {...form.getInputProps('company')}
        />
        <TextInput
            mt="md"
            label="Location"
            placeholder="Location"
            key={form.key('location')}
            withAsterisk
            {...form.getInputProps('location')}
        />
        <Select
            label="Contract"
            placeholder="Pick a Contract Type"
            data={['Full-Time', 'Part-Time', 'PhD', 'Internship']}
            key={form.key('contract')}
            {...form.getInputProps('contract')}
        />
        <Select
            label="Place"
            placeholder="Place"
            key={form.key('Place')}
            data={['Hybrid', 'On-Site', 'Remote']}
            {...form.getInputProps('place')}
        />
        <TagsInput
            label="Business"
            placeholder="Enter Business name"
            key={form.key("business")}
            data={["Software", "Research", "Biology", "Healthcare", "Consulting", "Communication", "Bank", "Finance"]}
            acceptValueOnBlur
            maxTags={3}
            {...form.getInputProps('business')}
        />
        <Select
            label="Status"
            placeholder="Pick a Status"
            data={Object.values(JobStatus)}
            key={form.key('status')}
            withAsterisk
            {...form.getInputProps('status')}
        />
        <DatePickerInput 
            label="Application Date"
            placeholder="Pick Application Date"
            value={dateValue} 
            onChange={handleDateChange}
        />
        <br/>
        <Button onClick={submitNewJob}>Add New Job</Button>
    </Modal> 
)}