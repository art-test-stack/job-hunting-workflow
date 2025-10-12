import { useContext, useState } from 'react';
import cx from 'clsx';
import {
    ActionIcon,
  Avatar,
  Button,
  Center,
  Checkbox,
  Group,
  keys,
  ScrollArea,
  Table,
  Text,
  TextInput,
  UnstyledButton,
} from '@mantine/core';
import { IconArticle, IconChevronDown, IconChevronUp, IconSearch, IconSelector } from '@tabler/icons-react';
import classes from './../styles/TableSort.module.css';

import Link from 'next/link';
import { JobOutput } from '@/client';
import { currentJobList } from '@/providers/jobs/jobListProvider';
import LoadingLayout from './loadingLayout';


interface ThProps {
    children: React.ReactNode;
    reversed: boolean;
    sorted: boolean;
    onSort: () => void;
}

function Th({ children, reversed, sorted, onSort }: ThProps) {
  const Icon = sorted ? (reversed ? IconChevronUp : IconChevronDown) : IconSelector;
  return (
    <Table.Th className={classes.th}>
      <UnstyledButton onClick={onSort} className={classes.control}>
        <Group justify="space-between">
          <Text fw={500} fz="sm">
            {children}
          </Text>
          <Center className={classes.icon}>
            <Icon size={16} stroke={1.5} />
          </Center>
        </Group>
      </UnstyledButton>
    </Table.Th>
  );
}

function filterData(data: JobOutput[], search: string) {
    if (!search) {
        return data
    }
  const query = search.toLowerCase().trim();
  return data.filter((item) =>
    keys(data[0]).some((key) => item[key] && item[key].toString().toLowerCase().includes(query))
  );
}

function sortData(
  data: JobOutput[],
  payload: { sortBy: keyof JobOutput | null; reversed: boolean; search: string }
) {
    const { sortBy } = payload;

    if (!sortBy) {
        return filterData(data, payload.search);
    }

    return filterData(
        [...data].sort((a, b) => {
        const aValue = Array.isArray(a[sortBy]) ? a[sortBy].join(', ') : a[sortBy];
        const bValue = Array.isArray(b[sortBy]) ? b[sortBy].join(', ') : b[sortBy];
        if (payload.reversed) {
            return (bValue ?? '').localeCompare(aValue ?? '');
        }
        return (aValue ?? '').localeCompare(bValue ?? '');
        }),
        payload.search
    );
}


export function JobsTable() {
    // const initialData = props.initialData
    const isLoading = false

    const [data, setData, loading] = useContext(currentJobList)

    if (loading) {
        return <LoadingLayout/>
    }
    const [search, setSearch] = useState('');
    const [sortedData, setSortedData] = useState(data);

    const [sortBy, setSortBy] = useState<keyof JobOutput | null>(null);
    const [reverseSortDirection, setReverseSortDirection] = useState(false);

    const [selection, setSelection] = useState<string[]>([]);

    const setSorting = (field: keyof JobOutput) => {
        const reversed = field === sortBy ? !reverseSortDirection : false;
        setReverseSortDirection(reversed);
        setSortBy(field);
        setSortedData(sortData([...data], { sortBy: field, reversed, search }));
        setSelection([]); // reset selection on new sort
    };

    const handleSearchChange = (query: React.ChangeEvent<HTMLInputElement>) => {
        console.log("typeof(query)", typeof(query));
        const value = query.currentTarget.value;
        console.log("value", value);
        setSearch(value);
    };

    const handleSearch = () => {
        setSortedData(sortData(sortedData, { sortBy, reversed: reverseSortDirection, search: search }));
        setSelection([]);
        setSortedData(sortData([...data], { sortBy, reversed: reverseSortDirection, search }));
    }

    const rows = sortedData.map((row: JobOutput) => {
        const selected = selection.includes(row.id);
        console.log("row.status",row.status)
        return (
        <Table.Tr key={row.id} className={cx({ [classes.rowSelected]: selected })}>
            <Table.Td>
                <ActionIcon 
                    component={Link} 
                    href={`/jobs/${row.id}`}
                >
                    <IconArticle/>
                </ActionIcon>
            </Table.Td>
            <Table.Td>{row.title}</Table.Td>
            <Table.Td>{row.company}</Table.Td>
            <Table.Td>{row.location}</Table.Td>
            <Table.Td>{row.contract}</Table.Td>
            <Table.Td>{row.place}</Table.Td>
            <Table.Td>{row.business}</Table.Td>
            <Table.Td>{row.status}</Table.Td>
            <Table.Td>{row.applied_at}</Table.Td>
            <Table.Td>
                {
                    row.url ?
                    <Link href={row.url}>Link
                    </Link> :
                    "No Link"
                }
            </Table.Td> 
        </Table.Tr>
        );
    });
    return (
        <>  
            <div>
                <TextInput
                    placeholder="Search by any field"
                    mb="md"
                    leftSection={<IconSearch size={16} stroke={1.5} />}
                    value={search}
                    onChange={(value) => handleSearchChange(value)}
                />
                <Button 
                    variant="default" 
                    onClick={handleSearch} 
                    leftSection={<IconSearch size={14}/>}
                    loading={isLoading}
                    disabled={search.length == 0}
                >   
                    Search
                </Button>
            </div>
            <ScrollArea>
                <Table 
                    striped 
                    highlightOnHover 
                    withColumnBorders 
                    miw={800} 
                    verticalSpacing="sm" 
                    horizontalSpacing="md"
                >
                    <Table.Thead>
                        <Table.Tr>
                            <Table.Th w={40}>
                                {/* <Checkbox
                                    onChange={toggleAll}
                                    checked={selection.length === sortedData.length && sortedData.length > 0}
                                    indeterminate={selection.length > 0 && selection.length !== sortedData.length}
                                /> */}
                            </Table.Th>
                            <Th
                                sorted={sortBy === 'title'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('title')}
                            >
                                Title
                            </Th>
                            <Th
                                sorted={sortBy === 'company'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('company')}
                            >
                                Company
                            </Th>
                            <Th
                                sorted={sortBy === 'location'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('location')}
                                >
                                Location
                            </Th>
                            <Th
                                sorted={sortBy === 'contract'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('contract')}
                                >
                                Contract
                            </Th>
                            <Th
                                sorted={sortBy === 'place'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('place')}
                                >
                                Type
                            </Th>
                            <Th
                                sorted={sortBy === 'business'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('business')}
                                >
                                Business
                            </Th>
                            <Th
                                sorted={sortBy === 'status'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('status')}
                                >
                                Status
                            </Th>
                            <Th
                                sorted={sortBy === 'applied_at'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('applied_at')}
                                >
                                Application Date
                            </Th>
                            <Th
                                sorted={sortBy === 'url'}
                                reversed={reverseSortDirection}
                                onSort={() => setSorting('url')}
                                >
                                URl
                            </Th>
                        </Table.Tr>
                    </Table.Thead>
                <Table.Tbody>
                {rows.length > 0 ? (
                    rows
                ) : (
                    <Table.Tr>
                    <Table.Td colSpan={10}>
                        <Text fw={500} ta="center">
                        No Job Found. Start by add a new job to your list.
                        </Text>
                    </Table.Td>
                    </Table.Tr>
                )}
                </Table.Tbody>
            </Table>
            </ScrollArea>
        </>
    );
}
