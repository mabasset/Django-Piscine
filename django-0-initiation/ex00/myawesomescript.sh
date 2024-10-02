#!/bin/sh

usage() {
	echo "Usage: $(basename ${0}) LINK." >&2
	echo "Displays the real address of a supposedly valid bit.ly address." >&2
	exit 1
}

if [ ${#} -ne 1 ]
then
	echo "$(basename ${0}): missing argument." >&2
	usage
fi

curl -Is ${1} | grep -i "location" | cut -d' ' -f2