import * as fs from 'fs';
import {CompactDictionaryBuilder} from "jsmigemo";

function containsSurrogatePair(s) {
    for (let i = 0; i < s.length; i++) {
        const codePoint = s.codePointAt(i);
        if (codePoint > 0xFFFF) {
            return true; // Found a character that is a surrogate pair
        }
        // If high surrogate, skip next char (the low surrogate)
        if (codePoint >= 0xD800 && codePoint <= 0xDBFF) {
            i++;
        }
    }
    return false;
}

// Read TSV file and build Map
const dictMap = new Map();
const tsvData = fs.readFileSync('migemo-dict', 'utf8');
const lines = tsvData.split('\n');

for (const line of lines) {
    const [key, ...values] = line.split('\t');
    if (key && values.length > 0) {
        // skip surrogate pair characters. Because rustmigemo doesn't support it.
        const filteredValues = values.filter(value => !containsSurrogatePair(value));
        if (filteredValues.length > 0) {
            dictMap.set(key, filteredValues);
        }
    }
}

// Compact Dictを構築する
const compactDict = CompactDictionaryBuilder.build(dictMap);

// 出力ファイルに書き込む
fs.writeFileSync('migemo-compact-dict', Buffer.from(compactDict));
