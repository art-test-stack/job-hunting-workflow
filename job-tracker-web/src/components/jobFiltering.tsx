import React, { useState } from 'react';
import { TextInput } from '@mantine/core';

export interface JobFilteringProps {
    searchTerm: string,
    setSearchTerm: CallableFunction
} 

export default function JobFiltering (props: JobFilteringProps) {
    return (
        <TextInput
            type="text"
            placeholder="Search jobs..."
            value={props.searchTerm}
            onChange={(e) => props.setSearchTerm(e.target.value)}
        />
    );
}