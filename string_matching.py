import time

def naiveSearch(pat, txt): # Naive
    M = len(pat)
    N = len(txt)
    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            print("Pattern found at index", i)

NO_OF_CHARS = 9192
 
def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar
 
def BMsearch(txt, pat): # Boyer-Moore
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            print("Pattern occur at shift = {}".format(s))
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])

if __name__ == '__main__':
    txt = "Bob Dylan (born Robert Allen Zimmerman; May 24, 1941) is an American singer-songwriter, author and visual artist. Often regarded as one of the greatest songwriters of all time, Dylan has been a major figure in popular culture during a career spanning nearly 60 years. Much of his most celebrated work dates from the 1960s, when songs such as 'Blowin in the Wind' (1963) and 'The Times They Are a-Changin' (1964) became anthems for the civil rights and anti-war movements. His lyrics during this period incorporated a range of political, social, philosophical, and literary influences, defying pop music conventions and appealing to the burgeoning counterculture. Following his self-titled debut album in 1962, which mainly comprised traditional folk songs, Dylan made his breakthrough as a songwriter with the release of The Freewheelin' Bob Dylan the following year. The album features 'Blowin' in the Wind' and the thematically complex 'A Hard Rain's a-Gonna Fall'. For many of these songs, he adapted the tunes and phraseology of older folk songs. He went on to release the politically charged The Times They Are a-Changin' and the more lyrically abstract and introspective Another Side of Bob Dylan in 1964. In 1965 and 1966, Dylan drew controversy when he adopted electrically amplified rock instrumentation, and in the space of 15 months recorded three of the most important and influential rock albums of the 1960s: Bringing It All Back Home (1965), Highway 61 Revisited (1965) and Blonde on Blonde (1966). Commenting on the six-minute single 'Like a Rolling Stone' (1965), Rolling Stone wrote: 'No other pop song has so thoroughly challenged and transformed the commercial laws and artistic conventions of its time, for all time.' In July 1966, a motorcycle accident led to Dylan's withdrawal from touring. During this period, he recorded a large body of songs with members of the Band, who had previously backed him on tour. These recordings were released as the collaborative album The Basement Tapes in 1975. In the late 1960s and early 1970s, Dylan explored country music and rural themes in John Wesley Harding (1967), Nashville Skyline (1969), and New Morning (1970). In 1975, he released Blood on the Tracks, which many saw as a return to form. In the late 1970s, he became a born-again Christian and released a series of albums of contemporary gospel music before returning to his more familiar rock-based idiom in the early 1980s. Dylan's 1997 album Time Out of Mind marked the beginning of a renaissance for his career. He has released five critically acclaimed albums of original material since then, the most recent being Rough and Rowdy Ways (2020). He also recorded a series of three albums in the 2010s comprising versions of traditional American standards, especially songs recorded by Frank Sinatra. Backed by a changing lineup of musicians, he has toured steadily since the late 1980s on what has been dubbed the Never Ending Tour."
    # txt = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    # patterns = song, time, most important, series of, author and visual artist, he recorded a large body of songs
    # list = ["song", "time", "most important", "series of", "author and visual artist", "he recorded a large body of songs"]
    list = ["Bob Dylan (born Robert Allen Zimmerman; May 24, 1941) is an American singer-songwriter, author and visual artist. Often regarded as one of the greatest songwriters of all time, Dylan has been a major figure in popular culture during a career spanning nearly 60 years. Much of his most celebrated work dates from the 1960s, when songs such as 'Blowin in the Wind' (1963) and 'The Times They Are a-Changin' (1964) became anthems for the civil rights and anti-war movements. His lyrics during this period incorporated a range of political, social, philosophical, and literary influences, defying pop music conventions and appealing to the burgeoning counterculture. Following his self-titled debut album in 1962, which mainly comprised traditional folk songs, Dylan made his breakthrough as a songwriter with the release of The Freewheelin' Bob Dylan the following year. The album features 'Blowin' in the Wind' and the thematically complex 'A Hard Rain's a-Gonna Fall'. For many of these songs, he adapted the tunes and phraseology of older folk songs. He went on to release the politically charged The Times They Are a-Changin' and the more lyrically abstract and introspective Another Side of Bob Dylan in 1964. In 1965 and 1966, Dylan drew controversy when he adopted electrically amplified rock instrumentation, and in the space of 15 months recorded three of the most important and influential rock albums of the 1960s: Bringing It All Back Home (1965), Highway 61 Revisited (1965) and Blonde on Blonde (1966). Commenting on the six-minute single 'Like a Rolling Stone' (1965), Rolling Stone wrote: 'No other pop song has so thoroughly challenged and transformed the commercial laws and artistic conventions of its time, for all time.' In July 1966, a motorcycle accident led to Dylan's withdrawal from touring. During this period, he recorded a large body of songs with members of the Band, who had previously backed him on tour. Tese recordings were released as the collaborative album The Basement Tapes in 1975. In the late 1960s and early 1970s, Dylan explored country music and rural themes in John Wesley Harding (1967), Nashville Skyline (1969), and New Morning (1970). In 1975, he released Blood on the Tracks, which many saw as a return to form. In the late 1970s, he became a born-again Christian and released a series of albums of contemporary gospel music before returning to his more familiar rock-based idiom in the early 1980s. Dylan's 1997 album Time Out of Mind marked the beginning of a renaissance for his career. He has released five critically acclaimed albums of original material since then, the most recent being Rough and Rowdy Ways (2020). He also recorded a series of three albums in the 2010s comprising versions of traditional American standards, especially songs recorded by Frank Sinatra. Backed by a changing lineup of musicians, he has toured steadily since the late 1980s on what has been dubbed the Never Ending Tour."]
    for obj in list:
        print("Finding '" + obj + "' in text...")
        start = time.time()
        naiveSearch(obj, txt)
        print("Time run by Naive Search: ",time.time() - start)
        start = time.time()
        BMsearch(txt, obj)
        print("Time run by Boyer-Moore Search: ",time.time() - start)
        print("")
    exit = input()