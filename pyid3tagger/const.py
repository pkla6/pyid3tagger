# coding=utf-8

__author__ = "Peter Klassen peter@mediadock.org"
__license__ = "MIT License"
__copyright__ = "(c) 2019 Peter Klassen peter@mediadock.org"

# versions
ID3v1_VERSION = 'ID3v1'
ID3v1_1_VERSION = 'ID3v1.1'
ID3v2_2_VERSION = 'ID3v2.2'
ID3v2_3_VERSION = 'ID3v2.3'
ID3v2_4_VERSION = 'ID3v2.4'


# ID3v1 genres
class ID3v1_GENERES(object):
    GENRE_2_NAME = dict()
    BLUES = 0
    BLUES_NAME = 'Blues'
    GENRE_2_NAME[BLUES] = BLUES_NAME
    CLASSIC_ROCK = 1
    CLASSIC_ROCK_NAME = 'Classic Rock'
    GENRE_2_NAME[CLASSIC_ROCK] = CLASSIC_ROCK_NAME
    COUNTY = 2
    COUNTY_NAME = 'Country'
    GENRE_2_NAME[COUNTY] = COUNTY_NAME
    DANCE = 3
    DANCE_NAME = 'Dance'
    GENRE_2_NAME[DANCE] = DANCE_NAME
    DISCO = 4
    DISCO_NAME = 'Disco'
    GENRE_2_NAME[DISCO] = DISCO_NAME
    FUNK = 5
    FUNK_NAME = 'Funk'
    GENRE_2_NAME[FUNK] = FUNK_NAME
    GRUNGE = 6
    GRUNGE_NAME = 'Grunge'
    GENRE_2_NAME[GRUNGE] = GRUNGE_NAME
    HIP_HOP = 7
    HIP_HOP_NAME = 'Hip-Hop'
    GENRE_2_NAME[HIP_HOP] = HIP_HOP_NAME
    JAZZ = 8
    JAZZ_NAME = 'Jazz'
    GENRE_2_NAME[JAZZ] = JAZZ_NAME
    METAL = 9
    METAL_NAME = 'Metal'
    GENRE_2_NAME[METAL] = METAL_NAME
    NEW_AGE = 10
    NEW_AGE_NAME = 'New Age'
    GENRE_2_NAME[NEW_AGE] = NEW_AGE_NAME
    OLDIES = 11
    OLDIES_NAME = 'Oldies'
    GENRE_2_NAME[OLDIES] = OLDIES_NAME
    OTHER = 12
    OTHER_NAME = 'Other'
    GENRE_2_NAME[OTHER] = OTHER_NAME
    POP = 13
    POP_NAME = 'Pop'
    GENRE_2_NAME[POP] = POP_NAME
    R_B = 14
    R_B_NAME = 'R&B'
    GENRE_2_NAME[R_B] = R_B_NAME
    RAP = 15
    RAP_NAME = 'Rap'
    GENRE_2_NAME[RAP] = RAP_NAME
    REGGAE = 16
    REGGAE_NAME = 'Reggae'
    GENRE_2_NAME[REGGAE] = REGGAE_NAME
    ROCK = 17
    ROCK_NAME = 'Rock'
    GENRE_2_NAME[ROCK] = ROCK_NAME
    TECHNO = 18
    TECHNO_NAME = 'Techno'
    GENRE_2_NAME[TECHNO] = TECHNO_NAME
    INDUSTRIAL = 19
    INDUSTRIAL_NAME = 'Industrial'
    GENRE_2_NAME[INDUSTRIAL] = INDUSTRIAL_NAME
    ALTERNATIVE = 20
    ALTERNATIVE_NAME = 'Alternative'
    GENRE_2_NAME[ALTERNATIVE] = ALTERNATIVE_NAME
    SKA = 21
    SKA_NAME = 'Ska'
    GENRE_2_NAME[SKA] = SKA_NAME
    DEATH_METAL = 22
    DEATH_METAL_NAME = 'Death Metal'
    GENRE_2_NAME[DEATH_METAL] = DEATH_METAL_NAME
    PRANKS = 23
    PRANKS_NAME = 'Pranks'
    GENRE_2_NAME[PRANKS] = PRANKS_NAME
    SOUNDTRACK = 24
    SOUNDTRACK_NAME = 'Soundtrack'
    GENRE_2_NAME[SOUNDTRACK] = SOUNDTRACK_NAME
    EURO_TECHNO = 25
    EURO_TECHNO_NAME = 'Euro-Techno'
    GENRE_2_NAME[EURO_TECHNO] = EURO_TECHNO_NAME
    AMBIENT = 26
    AMBIENT_NAME = 'Ambient'
    GENRE_2_NAME[AMBIENT] = AMBIENT_NAME
    TRIP_HOP = 27
    TRIP_HOP_NAME = 'Trip-Hop'
    GENRE_2_NAME[TRIP_HOP] = TRIP_HOP_NAME
    VOCAL = 28
    VOCAL_NAME = 'Vocal'
    GENRE_2_NAME[VOCAL] = VOCAL_NAME
    JAZZ_FUNK = 29
    JAZZ_FUNK_NAME = 'Jazz+Funk'
    GENRE_2_NAME[JAZZ_FUNK] = JAZZ_FUNK_NAME
    FUSION = 30
    FUSION_NAME = 'Fusion'
    GENRE_2_NAME[FUSION] = FUSION_NAME
    TRANCE = 31
    TRANCE_NAME = 'Trance'
    GENRE_2_NAME[TRANCE] = TRANCE_NAME
    CLASSICIAL = 32
    CLASSICIAL_NAME = 'Classical'
    GENRE_2_NAME[CLASSICIAL] = CLASSICIAL_NAME
    INSTRUMENTAL = 33
    INSTRUMENTAL_NAME = 'Instrumental'
    GENRE_2_NAME[INSTRUMENTAL] = INSTRUMENTAL_NAME
    ACID = 34
    ACID_NAME = 'Acid'
    GENRE_2_NAME[ACID] = ACID_NAME
    HOUSE = 35
    HOUSE_NAME = 'House'
    GENRE_2_NAME[HOUSE] = HOUSE_NAME
    GAME = 36
    GAME_NAME = 'Game'
    GENRE_2_NAME[GAME] = GAME_NAME
    SOUND_CLIP = 37
    SOUND_CLIP_NAME = 'Sound Clip'
    GENRE_2_NAME[SOUND_CLIP] = SOUND_CLIP_NAME
    GOSPEL = 38
    GOSPEL_NAME = 'Gospel'
    GENRE_2_NAME[GOSPEL] = GOSPEL_NAME
    NOISE = 39
    NOISE_NAME = 'Noise'
    GENRE_2_NAME[NOISE] = NOISE_NAME
    ALTERNROCK = 40
    ALTERNROCK_NAME = 'AlternRock'
    GENRE_2_NAME[ALTERNROCK] = ALTERNROCK_NAME
    BASS = 41
    BASS_NAME = 'Bass'
    GENRE_2_NAME[BASS] = BASS_NAME
    SOUL = 42
    SOUL_NAME = 'Soul'
    GENRE_2_NAME[SOUL] = SOUL_NAME
    PUNK = 43
    PUNK_NAME = 'Punk'
    GENRE_2_NAME[PUNK] = PUNK_NAME
    SPACE = 44
    SPACE_NAME = 'Space'
    GENRE_2_NAME[SPACE] = SPACE_NAME
    MEDITATIVE = 45
    MEDITATIVE_NAME = 'Meditative'
    GENRE_2_NAME[MEDITATIVE] = MEDITATIVE_NAME
    INSTRUMENTAL_POP = 46
    INSTRUMENTAL_POP_NAME = 'Instrumental Pop'
    GENRE_2_NAME[INSTRUMENTAL_POP] = INSTRUMENTAL_POP_NAME
    INSTRUMENTAL_ROCK = 47
    INSTRUMENTAL_ROCK_NAME = 'Instrumental Rock'
    GENRE_2_NAME[INSTRUMENTAL_ROCK] = INSTRUMENTAL_ROCK_NAME
    ETHNIC = 48
    ETHNIC_NAME = 'Ethnic'
    GENRE_2_NAME[ETHNIC] = ETHNIC_NAME
    GOTHIC = 49
    GOTHIC_NAME = 'Gothic'
    GENRE_2_NAME[GOTHIC] = GOTHIC_NAME
    DARKWAVE = 50
    DARKWAVE_NAME = 'Darkwave'
    GENRE_2_NAME[DARKWAVE] = DARKWAVE_NAME
    TECHNO_INDUSTRIAL = 51
    TECHNO_INDUSTRIAL_NAME = 'Techno-Industrial'
    GENRE_2_NAME[TECHNO_INDUSTRIAL] = TECHNO_INDUSTRIAL_NAME
    ELECTRONIC = 52
    ELECTRONIC_NAME = 'Electronic'
    GENRE_2_NAME[ELECTRONIC] = ELECTRONIC_NAME
    POP_FOLK = 53
    POP_FOLK_NAME = 'Pop-Folk'
    GENRE_2_NAME[POP_FOLK] = POP_FOLK_NAME
    EURODANCE = 54
    EURODANCE_NAME = 'Eurodance'
    GENRE_2_NAME[EURODANCE] = EURODANCE_NAME
    DREAM = 55
    DREAM_NAME = 'Dream'
    GENRE_2_NAME[DREAM] = DREAM_NAME
    SOUTHERN_ROCK = 56
    SOUTHERN_ROCK_NAME = 'Southern Rock'
    GENRE_2_NAME[SOUTHERN_ROCK] = SOUTHERN_ROCK_NAME
    COMEDY = 57
    COMEDY_NAME = 'Comedy'
    GENRE_2_NAME[COMEDY] = COMEDY_NAME
    CULT = 58
    CULT_NAME = 'Cult'
    GENRE_2_NAME[CULT] = CULT_NAME
    GANGSTA = 59
    GANGSTA_NAME = 'Gangsta'
    GENRE_2_NAME[GANGSTA] = GANGSTA_NAME
    TOP_40 = 60
    TOP_40_NAME = 'Top 40'
    GENRE_2_NAME[TOP_40] = TOP_40_NAME
    CHRISTIAN_RAP = 61
    CHRISTIAN_RAP_NAME = 'Christian Rap'
    GENRE_2_NAME[CHRISTIAN_RAP] = CHRISTIAN_RAP_NAME
    POP_FUNK = 62
    POP_FUNK_NAME = 'Pop/Funk'
    GENRE_2_NAME[POP_FUNK] = POP_FUNK_NAME
    JUNGLE = 63
    JUNGLE_NAME = 'Jungle'
    GENRE_2_NAME[JUNGLE] = JUNGLE_NAME
    NATIVE_AMERICAN = 64
    NATIVE_AMERICAN_NAME = 'Native American'
    GENRE_2_NAME[NATIVE_AMERICAN] = NATIVE_AMERICAN_NAME
    CABARET = 65
    CABARET_NAME = 'Cabaret'
    GENRE_2_NAME[CABARET] = CABARET_NAME
    NEW_WAVE = 66
    NEW_WAVE_NAME = 'New Wave'
    GENRE_2_NAME[NEW_WAVE] = NEW_WAVE_NAME
    PSYCHADELIC = 67
    PSYCHADELIC_NAME = 'Psychadelic'
    GENRE_2_NAME[PSYCHADELIC] = PSYCHADELIC_NAME
    RAVE = 68
    RAVE_NAME = 'Rave'
    GENRE_2_NAME[RAVE] = RAVE_NAME
    SHOWTUNES = 69
    SHOWTUNES_NAME = 'Showtunes'
    GENRE_2_NAME[SHOWTUNES] = SHOWTUNES_NAME
    TRAILER = 70
    TRAILER_NAME = 'Trailer'
    GENRE_2_NAME[TRAILER] = TRAILER_NAME
    LO_FI = 71
    LO_FI_NAME = 'Lo-Fi'
    GENRE_2_NAME[LO_FI] = LO_FI_NAME
    TRIBAL = 72
    TRIBAL_NAME = 'Tribal'
    GENRE_2_NAME[TRIBAL] = TRIBAL_NAME
    ACID_PUNK = 73
    ACID_PUNK_NAME = 'Acid Punk'
    GENRE_2_NAME[ACID_PUNK] = ACID_PUNK_NAME
    ACID_JAZZ = 74
    ACID_JAZZ_NAME = 'Acid Jazz'
    GENRE_2_NAME[ACID_JAZZ] = ACID_JAZZ_NAME
    POLKA = 75
    POLKA_NAME = 'Polka'
    GENRE_2_NAME[POLKA] = POLKA_NAME
    RETRO = 76
    RETRO_NAME = 'Retro'
    GENRE_2_NAME[RETRO] = RETRO_NAME
    MUSICAL = 77
    MUSICAL_NAME = 'Musical'
    GENRE_2_NAME[MUSICAL] = MUSICAL_NAME
    ROCK_N_ROLL = 78
    ROCK_N_ROLL_NAME = 'Rock & Roll'
    GENRE_2_NAME[ROCK_N_ROLL] = ROCK_N_ROLL_NAME
    HARD_ROCK = 79
    HARD_ROCK_NAME = 'Hard Rock'
    GENRE_2_NAME[HARD_ROCK] = HARD_ROCK_NAME
    FOLK = 80
    FOLK_NAME = 'Folk'
    GENRE_2_NAME[FOLK] = FOLK_NAME
    FOLK_ROCK = 81
    FOLK_ROCK_NAME = 'Folk-Rock'
    GENRE_2_NAME[FOLK_ROCK] = FOLK_ROCK_NAME
    NATIONAL_FOLK = 82
    NATIONAL_FOLK_NAME = 'National Folk'
    GENRE_2_NAME[NATIONAL_FOLK] = NATIONAL_FOLK_NAME
    SWING = 83
    SWING_NAME = 'Swing'
    GENRE_2_NAME[SWING] = SWING_NAME
    FAST_FUSION = 84
    FAST_FUSION_NAME = 'Fast Fusion'
    GENRE_2_NAME[FAST_FUSION] = FAST_FUSION_NAME
    BEBOB = 85
    BEBOB_NAME = 'Bebob'
    GENRE_2_NAME[BEBOB] = BEBOB_NAME
    LATIN = 86
    LATIN_NAME = 'Latin'
    GENRE_2_NAME[LATIN] = LATIN_NAME
    REVIVAL = 87
    REVIVAL_NAME = 'Revival'
    GENRE_2_NAME[REVIVAL] = REVIVAL_NAME
    CELTIC = 88
    CELTIC_NAME = 'Celtic'
    GENRE_2_NAME[CELTIC] = CELTIC_NAME
    BLUEGRASS = 89
    BLUEGRASS_NAME = 'Bluegrass'
    GENRE_2_NAME[BLUEGRASS] = BLUEGRASS_NAME
    AVANTGARDE = 90
    AVANTGARDE_NAME = 'Avantgarde'
    GENRE_2_NAME[AVANTGARDE] = AVANTGARDE_NAME
    GOTHIC_ROCK = 91
    GOTHIC_ROCK_NAME = 'Gothic Rock'
    GENRE_2_NAME[GOTHIC_ROCK] = GOTHIC_ROCK_NAME
    PROGRESSIVE_ROCK = 92
    PROGRESSIVE_ROCK_NAME = 'Progressive Rock'
    GENRE_2_NAME[PROGRESSIVE_ROCK] = PROGRESSIVE_ROCK_NAME
    PSYCHEDELIC_ROCK = 93
    PSYCHEDELIC_ROCK_NAME = 'Psychedelic Rock'
    GENRE_2_NAME[PSYCHEDELIC_ROCK] = PSYCHEDELIC_ROCK_NAME
    SYMPHONIC_ROCK = 94
    SYMPHONIC_ROCK_NAME = 'Symphonic Rock'
    GENRE_2_NAME[SYMPHONIC_ROCK] = SYMPHONIC_ROCK_NAME
    SLOW_ROCK = 95
    SLOW_ROCK_NAME = 'Slow Rock'
    GENRE_2_NAME[SLOW_ROCK] = SLOW_ROCK_NAME
    BIG_BAND = 96
    BIG_BAND_NAME = 'Big Band'
    GENRE_2_NAME[BIG_BAND] = BIG_BAND_NAME
    CHORUS = 97
    CHORUS_NAME = 'Chorus'
    GENRE_2_NAME[CHORUS] = CHORUS_NAME
    EASY_LISTENING = 98
    EASY_LISTENING_NAME = 'Easy Listening'
    GENRE_2_NAME[EASY_LISTENING] = EASY_LISTENING_NAME
    ACOUSTIC = 99
    ACOUSTIC_NAME = 'Acoustic'
    GENRE_2_NAME[ACOUSTIC] = ACOUSTIC_NAME
    HUMOR = 100
    HUMOR_NAME = 'Humour'
    GENRE_2_NAME[HUMOR] = HUMOR_NAME
    SPEECH = 101
    SPEECH_NAME = 'Speech'
    GENRE_2_NAME[SPEECH] = SPEECH_NAME
    CHANSON = 102
    CHANSON_NAME = 'Chanson'
    GENRE_2_NAME[CHANSON] = CHANSON_NAME
    OPERA = 103
    OPERA_NAME = 'Opera'
    GENRE_2_NAME[OPERA] = OPERA_NAME
    CHAMBER_MUSIC = 104
    CHAMBER_MUSIC_NAME = 'Chamber Music'
    GENRE_2_NAME[CHAMBER_MUSIC] = CHAMBER_MUSIC_NAME
    SONATA = 105
    SONATA_NAME = 'Sonata'
    GENRE_2_NAME[SONATA] = SONATA_NAME
    SYMPHONY = 106
    SYMPHONY_NAME = 'Symphony'
    GENRE_2_NAME[SYMPHONY] = SYMPHONY_NAME
    BOOTY_BASS = 107
    BOOTY_BASS_NAME = 'Booty Bass'
    GENRE_2_NAME[BOOTY_BASS] = BOOTY_BASS_NAME
    PRIMUS = 108
    PRIMUS_NAME = 'Primus'
    GENRE_2_NAME[PRIMUS] = PRIMUS_NAME
    PORN_GROOVE = 109
    PORN_GROOVE_NAME = 'Porn Groove'
    GENRE_2_NAME[PORN_GROOVE] = PORN_GROOVE_NAME
    SATRIRE = 110
    SATRIRE_NAME = 'Satire'
    GENRE_2_NAME[SATRIRE] = SATRIRE_NAME
    SLOW_JAM = 111
    SLOW_JAM_NAME = 'Slow Jam'
    GENRE_2_NAME[SLOW_JAM] = SLOW_JAM_NAME
    CLUB = 112
    CLUB_NAME = 'Club'
    GENRE_2_NAME[CLUB] = CLUB_NAME
    TANGO = 113
    TANGO_NAME = 'Tango'
    GENRE_2_NAME[TANGO] = TANGO_NAME
    SAMBA = 114
    SAMBA_NAME = 'Samba'
    GENRE_2_NAME[SAMBA] = SAMBA_NAME
    FOLKLORE = 115
    FOLKLORE_NAME = 'Folklore'
    GENRE_2_NAME[FOLKLORE] = FOLKLORE_NAME
    BALLAD = 116
    BALLAD_NAME = 'Ballad'
    GENRE_2_NAME[BALLAD] = BALLAD_NAME
    POWER_BALLAD = 117
    POWER_BALLAD_NAME = 'Power Ballad'
    GENRE_2_NAME[POWER_BALLAD] = POWER_BALLAD_NAME
    RHYTHMIC_SOUL = 118
    RHYTHMIC_SOUL_NAME = 'Rhythmic Soul'
    GENRE_2_NAME[RHYTHMIC_SOUL] = RHYTHMIC_SOUL_NAME
    FREESTYLE = 119
    FREESTYLE_NAME = 'Freestyle'
    GENRE_2_NAME[FREESTYLE] = FREESTYLE_NAME
    DUET = 120
    DUET_NAME = 'Duet'
    GENRE_2_NAME[DUET] = DUET_NAME
    PUNK_ROCK = 121
    PUNK_ROCK_NAME = 'Punk Rock'
    GENRE_2_NAME[PUNK_ROCK] = PUNK_ROCK_NAME
    DRUM_SOLO = 122
    DRUM_SOLO_NAME = 'Drum Solo'
    GENRE_2_NAME[DRUM_SOLO] = DRUM_SOLO_NAME
    A_CAPELLA = 123
    A_CAPELLA_NAME = 'A capella'
    GENRE_2_NAME[A_CAPELLA] = A_CAPELLA_NAME
    EURO_HOUSE = 124
    EURO_HOUSE_NAME = 'Euro-House'
    GENRE_2_NAME[EURO_HOUSE] = EURO_HOUSE_NAME
    DANCE_HALL = 125
    DANCE_HALL_NAME = 'Dance Hall'
    GENRE_2_NAME[DANCE_HALL] = DANCE_HALL_NAME
    GOA = 126
    GOA_NAME = 'Goa'
    GENRE_2_NAME[GOA] = GOA_NAME
    DRUM_N_BASS = 127
    DRUM_N_BASS_NAME = 'Drum & Bass'
    GENRE_2_NAME[DRUM_N_BASS] = DRUM_N_BASS_NAME
    CLUB_HOUSE = 128
    CLUB_HOUSE_NAME = 'Club-House'
    GENRE_2_NAME[CLUB_HOUSE] = CLUB_HOUSE_NAME
    HARDCORE = 129
    HARDCORE_NAME = 'Hardcore'
    GENRE_2_NAME[HARDCORE] = HARDCORE_NAME
    TERROR = 130
    TERROR_NAME = 'Terror'
    GENRE_2_NAME[TERROR] = TERROR_NAME
    INDIE = 131
    INDIE_NAME = 'Indie'
    GENRE_2_NAME[INDIE] = INDIE_NAME
    BRITPOP = 132
    BRITPOP_NAME = 'BritPop'
    GENRE_2_NAME[BRITPOP] = BRITPOP_NAME
    NEGERPUNK = 133
    NEGERPUNK_NAME = 'Negerpunk'
    GENRE_2_NAME[NEGERPUNK] = NEGERPUNK_NAME
    POLSK_PUNK = 134
    POLSK_PUNK_NAME = 'Polsk Punk'
    GENRE_2_NAME[POLSK_PUNK] = POLSK_PUNK_NAME
    BEAT = 135
    BEAT_NAME = 'Beat'
    GENRE_2_NAME[BEAT] = BEAT_NAME
    CHRISTIAN = 136
    CHRISTIAN_NAME = 'Christian'
    GENRE_2_NAME[CHRISTIAN] = CHRISTIAN_NAME
    HEAVY_METAL = 137
    HEAVY_METAL_NAME = 'Heavy Metal'
    GENRE_2_NAME[HEAVY_METAL] = HEAVY_METAL_NAME
    BLACK_METAL = 138
    BLACK_METAL_NAME = 'Black Metal'
    GENRE_2_NAME[BLACK_METAL] = BLACK_METAL_NAME
    CROSSOVER = 139
    CROSSOVER_NAME = 'Crossover'
    GENRE_2_NAME[CROSSOVER] = CROSSOVER_NAME
    CONTEMPORARY = 140
    CONTEMPORARY_NAME = 'Contemporary'
    GENRE_2_NAME[CONTEMPORARY] = CONTEMPORARY_NAME
    CHRISTIAN_ROCK = 141
    CHRISTIAN_ROCK_NAME = 'Christian Rock'
    GENRE_2_NAME[CHRISTIAN_ROCK] = CHRISTIAN_ROCK_NAME
    MERENGUE = 142
    MERENGUE_NAME = 'Merengue'
    GENRE_2_NAME[MERENGUE] = MERENGUE_NAME
    SALSA = 143
    SALSA_NAME = 'Salsa'
    GENRE_2_NAME[SALSA] = SALSA_NAME
    THRASH_METAL = 144
    THRASH_METAL_NAME = 'Thrash Metal'
    GENRE_2_NAME[THRASH_METAL] = THRASH_METAL_NAME
    ANIME = 145
    ANIME_NAME = 'Anime'
    GENRE_2_NAME[ANIME] = ANIME_NAME
    JPOP = 146
    JPOP_NAME = 'JPop'
    GENRE_2_NAME[JPOP] = JPOP_NAME
    SYNTHPOP = 147
    SYNTHPOP_NAME = 'Synthpop'
    GENRE_2_NAME[SYNTHPOP] = SYNTHPOP_NAME


class ID3v2_3ENCODING(object):
    ISO_8859_1 = '\x00'
    UNICODE = '\x01'


ID3v2_3_ENCODING_DICT = {ID3v2_3ENCODING.ISO_8859_1: 'latin-1', ID3v2_3ENCODING.UNICODE: 'utf-16'}

LANGUAGE_CODES_ISO_639_2_DICT = {
    'aar': 'Afar',
    'abk': 'Abkhazian',
    'ace': 'Achinese',
    'ach': 'Acoli',
    'ada': 'Adangme',
    'ady': 'Adyghe; Adygei',
    'afa': 'Afro-Asiatic languages',
    'afh': 'Afrihili',
    'afr': 'Afrikaans',
    'ain': 'Ainu',
    'aka': 'Akan',
    'akk': 'Akkadian',
    'alb': 'Albanian',
    'ale': 'Aleut',
    'alg': 'Algonquian languages',
    'alt': 'Southern Altai',
    'amh': 'Amharic',
    'ang': 'English, Old (ca.450-1100)',
    'anp': 'Angika',
    'apa': 'Apache languages',
    'ara': 'Arabic',
    'arc': 'Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)',
    'arg': 'Aragonese',
    'arm': 'Armenian',
    'arn': 'Mapudungun; Mapuche',
    'arp': 'Arapaho',
    'art': 'Artificial languages',
    'arw': 'Arawak',
    'asm': 'Assamese',
    'ast': 'Asturian; Bable; Leonese; Asturleonese',
    'ath': 'Athapascan languages',
    'aus': 'Australian languages',
    'ava': 'Avaric',
    'ave': 'Avestan',
    'awa': 'Awadhi',
    'aym': 'Aymara',
    'aze': 'Azerbaijani',
    'bad': 'Banda languages',
    'bai': 'Bamileke languages',
    'bak': 'Bashkir',
    'bal': 'Baluchi',
    'bam': 'Bambara',
    'ban': 'Balinese',
    'baq': 'Basque',
    'bas': 'Basa',
    'bat': 'Baltic languages',
    'bej': 'Beja; Bedawiyet',
    'bel': 'Belarusian',
    'bem': 'Bemba',
    'ben': 'Bengali',
    'ber': 'Berber languages',
    'bho': 'Bhojpuri',
    'bih': 'Bihari languages',
    'bik': 'Bikol',
    'bin': 'Bini; Edo',
    'bis': 'Bislama',
    'bla': 'Siksika',
    'bnt': 'Bantu languages',
    'bod': 'Tibetan',
    'bos': 'Bosnian',
    'bra': 'Braj',
    'bre': 'Breton',
    'btk': 'Batak languages',
    'bua': 'Buriat',
    'bug': 'Buginese',
    'bul': 'Bulgarian',
    'bur': 'Burmese',
    'byn': 'Blin; Bilin',
    'cad': 'Caddo',
    'cai': 'Central American Indian languages',
    'car': 'Galibi Carib',
    'cat': 'Catalan; Valencian',
    'cau': 'Caucasian languages',
    'ceb': 'Cebuano',
    'cel': 'Celtic languages',
    'ces': 'Czech',
    'cha': 'Chamorro',
    'chb': 'Chibcha',
    'che': 'Chechen',
    'chg': 'Chagatai',
    'chi': 'Chinese',
    'chk': 'Chuukese',
    'chm': 'Mari',
    'chn': 'Chinook jargon',
    'cho': 'Choctaw',
    'chp': 'Chipewyan; Dene Suline',
    'chr': 'Cherokee',
    'chu': 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic',
    'chv': 'Chuvash',
    'chy': 'Cheyenne',
    'cmc': 'Chamic languages',
    'cnr': 'Montenegrin',
    'cop': 'Coptic',
    'cor': 'Cornish',
    'cos': 'Corsican',
    'cpe': 'Creoles and pidgins, English based',
    'cpf': 'Creoles and pidgins, French-based',
    'cpp': 'Creoles and pidgins, Portuguese-based',
    'cre': 'Cree',
    'crh': 'Crimean Tatar; Crimean Turkish',
    'crp': 'Creoles and pidgins',
    'csb': 'Kashubian',
    'cus': 'Cushitic languages',
    'cym': 'Welsh',
    'cze': 'Czech',
    'dak': 'Dakota',
    'dan': 'Danish',
    'dar': 'Dargwa',
    'day': 'Land Dayak languages',
    'del': 'Delaware',
    'den': 'Slave (Athapascan)',
    'deu': 'German',
    'dgr': 'Dogrib',
    'din': 'Dinka',
    'div': 'Divehi; Dhivehi; Maldivian',
    'doi': 'Dogri',
    'dra': 'Dravidian languages',
    'dsb': 'Lower Sorbian',
    'dua': 'Duala',
    'dum': 'Dutch, Middle (ca.1050-1350)',
    'dut': 'Dutch; Flemish',
    'dyu': 'Dyula',
    'dzo': 'Dzongkha',
    'efi': 'Efik',
    'egy': 'Egyptian (Ancient)',
    'eka': 'Ekajuk',
    'ell': 'Greek, Modern (1453-)',
    'elx': 'Elamite',
    'eng': 'English',
    'enm': 'English, Middle (1100-1500)',
    'epo': 'Esperanto',
    'est': 'Estonian',
    'eus': 'Basque',
    'ewe': 'Ewe',
    'ewo': 'Ewondo',
    'fan': 'Fang',
    'fao': 'Faroese',
    'fas': 'Persian',
    'fat': 'Fanti',
    'fij': 'Fijian',
    'fil': 'Filipino; Pilipino',
    'fin': 'Finnish',
    'fiu': 'Finno-Ugrian languages',
    'fon': 'Fon',
    'fre': 'French',
    'fra': 'French',
    'frm': 'French, Middle (ca.1400-1600)',
    'fro': 'French, Old (842-ca.1400)',
    'frr': 'Northern Frisian',
    'frs': 'Eastern Frisian',
    'fry': 'Western Frisian',
    'ful': 'Fulah',
    'fur': 'Friulian',
    'gaa': 'Ga',
    'gay': 'Gayo',
    'gba': 'Gbaya',
    'gem': 'Germanic languages',
    'geo': 'Georgian',
    'ger': 'German',
    'gez': 'Geez',
    'gil': 'Gilbertese',
    'gla': 'Gaelic; Scottish Gaelic',
    'gle': 'Irish',
    'glg': 'Galician',
    'glv': 'Manx',
    'gmh': 'German, Middle High (ca.1050-1500)',
    'goh': 'German, Old High (ca.750-1050)',
    'gon': 'Gondi',
    'gor': 'Gorontalo',
    'got': 'Gothic',
    'grb': 'Grebo',
    'grc': 'Greek, Ancient (to 1453)',
    'gre': 'Greek, Modern (1453-)',
    'grn': 'Guarani',
    'gsw': 'Swiss German; Alemannic; Alsatian',
    'guj': 'Gujarati',
    'gwi': 'Gwich\'in',
    'hai': 'Haida',
    'hat': 'Haitian; Haitian Creole',
    'hau': 'Hausa',
    'haw': 'Hawaiian',
    'heb': 'Hebrew',
    'her': 'Herero',
    'hil': 'Hiligaynon',
    'him': 'Himachali languages; Western Pahari languages',
    'hin': 'Hindi',
    'hit': 'Hittite',
    'hmn': 'Hmong; Mong',
    'hmo': 'Hiri Motu',
    'hrv': 'Croatian',
    'hsb': 'Upper Sorbian',
    'hun': 'Hungarian',
    'hup': 'Hupa',
    'hye': 'Armenian',
    'iba': 'Iban',
    'ibo': 'Igbo',
    'ice': 'Icelandic',
    'isl': 'Icelandic',
    'ido': 'Ido',
    'iii': 'Sichuan Yi; Nuosu',
    'ijo': 'Ijo languages',
    'iku': 'Inuktitut',
    'ile': 'Interlingue; Occidental',
    'ilo': 'Iloko',
    'ina': 'Interlingua (International Auxiliary Language Association)',
    'inc': 'Indic languages',
    'ind': 'Indonesian',
    'ine': 'Indo-European languages',
    'inh': 'Ingush',
    'ipk': 'Inupiaq',
    'ira': 'Iranian languages',
    'iro': 'Iroquoian languages',
    'ita': 'Italian',
    'jav': 'Javanese',
    'jbo': 'Lojban',
    'jpn': 'Japanese',
    'jpr': 'Judeo-Persian',
    'jrb': 'Judeo-Arabic',
    'kaa': 'Kara-Kalpak',
    'kab': 'Kabyle',
    'kac': 'Kachin; Jingpho',
    'kal': 'Kalaallisut; Greenlandic',
    'kam': 'Kamba',
    'kan': 'Kannada',
    'kar': 'Karen languages',
    'kas': 'Kashmiri',
    'kat': 'Georgian',
    'kau': 'Kanuri',
    'kaw': 'Kawi',
    'kaz': 'Kazakh',
    'kbd': 'Kabardian',
    'kha': 'Khasi',
    'khi': 'Khoisan languages',
    'khm': 'Central Khmer',
    'kho': 'Khotanese; Sakan',
    'kik': 'Kikuyu; Gikuyu',
    'kin': 'Kinyarwanda',
    'kir': 'Kirghiz; Kyrgyz',
    'kmb': 'Kimbundu',
    'kok': 'Konkani',
    'kom': 'Komi',
    'kon': 'Kongo',
    'kor': 'Korean',
    'kos': 'Kosraean',
    'kpe': 'Kpelle',
    'krc': 'Karachay-Balkar',
    'krl': 'Karelian',
    'kro': 'Kru languages',
    'kru': 'Kurukh',
    'kua': 'Kuanyama; Kwanyama',
    'kum': 'Kumyk',
    'kur': 'Kurdish',
    'kut': 'Kutenai',
    'lad': 'Ladino',
    'lah': 'Lahnda',
    'lam': 'Lamba',
    'lao': 'Lao',
    'lat': 'Latin',
    'lav': 'Latvian',
    'lez': 'Lezghian',
    'lim': 'Limburgan; Limburger; Limburgish',
    'lin': 'Lingala',
    'lit': 'Lithuanian',
    'lol': 'Mongo',
    'loz': 'Lozi',
    'ltz': 'Luxembourgish; Letzeburgesch',
    'lua': 'Luba-Lulua',
    'lub': 'Luba-Katanga',
    'lug': 'Ganda',
    'lui': 'Luiseno',
    'lun': 'Lunda',
    'luo': 'Luo (Kenya and Tanzania)',
    'lus': 'Lushai',
    'mac': 'Macedonian',
    'mad': 'Madurese',
    'mag': 'Magahi',
    'mah': 'Marshallese',
    'mai': 'Maithili',
    'mak': 'Makasar',
    'mal': 'Malayalam',
    'man': 'Mandingo',
    'mao': 'Maori',
    'map': 'Austronesian languages',
    'mar': 'Marathi',
    'mas': 'Masai',
    'may': 'Malay',
    'mdf': 'Moksha',
    'mdr': 'Mandar',
    'men': 'Mende',
    'mga': 'Irish, Middle (900-1200)',
    'mic': 'Mi\'kmaq; Micmac',
    'min': 'Minangkabau',
    'mis': 'Uncoded languages',
    'mkd': 'Macedonian',
    'mkh': 'Mon-Khmer languages',
    'mlg': 'Malagasy',
    'mlt': 'Maltese',
    'mnc': 'Manchu',
    'mni': 'Manipuri',
    'mno': 'Manobo languages',
    'moh': 'Mohawk',
    'mon': 'Mongolian',
    'mos': 'Mossi',
    'mri': 'Maori',
    'msa': 'Malay',
    'mul': 'Multiple languages',
    'mun': 'Munda languages',
    'mus': 'Creek',
    'mwl': 'Mirandese',
    'mwr': 'Marwari',
    'mya': 'Burmese',
    'myn': 'Mayan languages',
    'myv': 'Erzya',
    'nah': 'Nahuatl languages',
    'nai': 'North American Indian languages',
    'nap': 'Neapolitan',
    'nau': 'Nauru',
    'nav': 'Navajo; Navaho',
    'nbl': 'Ndebele, South; South Ndebele',
    'nde': 'Ndebele, North; North Ndebele',
    'ndo': 'Ndonga',
    'nds': 'Low German; Low Saxon; German, Low; Saxon, Low',
    'nep': 'Nepali',
    'new': 'Nepal Bhasa; Newari',
    'nia': 'Nias',
    'nic': 'Niger-Kordofanian languages',
    'niu': 'Niuean',
    'nld': 'Dutch; Flemish',
    'nno': 'Norwegian Nynorsk; Nynorsk, Norwegian',
    'nob': 'Bokmål, Norwegian; Norwegian Bokmål',
    'nog': 'Nogai',
    'non': 'Norse, Old',
    'nor': 'Norwegian',
    'nqo': 'N\'Ko',
    'nso': 'Pedi; Sepedi; Northern Sotho',
    'nub': 'Nubian languages',
    'nwc': 'Classical Newari; Old Newari; Classical Nepal Bhasa',
    'nya': 'Chichewa; Chewa; Nyanja',
    'nym': 'Nyamwezi',
    'nyn': 'Nyankole',
    'nyo': 'Nyoro',
    'nzi': 'Nzima',
    'oci': 'Occitan (post 1500)',
    'oji': 'Ojibwa',
    'ori': 'Oriya',
    'orm': 'Oromo',
    'osa': 'Osage',
    'oss': 'Ossetian; Ossetic',
    'ota': 'Turkish, Ottoman (1500-1928)',
    'oto': 'Otomian languages',
    'paa': 'Papuan languages',
    'pag': 'Pangasinan',
    'pal': 'Pahlavi',
    'pam': 'Pampanga; Kapampangan',
    'pan': 'Panjabi; Punjabi',
    'pap': 'Papiamento',
    'pau': 'Palauan',
    'peo': 'Persian, Old (ca.600-400 B.C.)',
    'per': 'Persian',
    'phi': 'Philippine languages',
    'phn': 'Phoenician',
    'pli': 'Pali',
    'pol': 'Polish',
    'pon': 'Pohnpeian',
    'por': 'Portuguese',
    'pra': 'Prakrit languages',
    'pro': 'Provençal, Old (to 1500);Occitan, Old (to 1500)',
    'pus': 'Pushto; Pashto',
    'qaa': 'Reserved for local use',
    'qab': 'Reserved for local use',
    'qac': 'Reserved for local use',
    'qad': 'Reserved for local use',
    'qae': 'Reserved for local use',
    'qaf': 'Reserved for local use',
    'qag': 'Reserved for local use',
    'qah': 'Reserved for local use',
    'qai': 'Reserved for local use',
    'qaj': 'Reserved for local use',
    'qak': 'Reserved for local use',
    'qal': 'Reserved for local use',
    'qam': 'Reserved for local use',
    'qan': 'Reserved for local use',
    'qao': 'Reserved for local use',
    'qap': 'Reserved for local use',
    'qaq': 'Reserved for local use',
    'qar': 'Reserved for local use',
    'qas': 'Reserved for local use',
    'qat': 'Reserved for local use',
    'qau': 'Reserved for local use',
    'qav': 'Reserved for local use',
    'qaw': 'Reserved for local use',
    'qax': 'Reserved for local use',
    'qay': 'Reserved for local use',
    'qaz': 'Reserved for local use',
    'qba': 'Reserved for local use',
    'qbb': 'Reserved for local use',
    'qbc': 'Reserved for local use',
    'qbd': 'Reserved for local use',
    'qbe': 'Reserved for local use',
    'qbf': 'Reserved for local use',
    'qbg': 'Reserved for local use',
    'qbh': 'Reserved for local use',
    'qbi': 'Reserved for local use',
    'qbj': 'Reserved for local use',
    'qbk': 'Reserved for local use',
    'qbl': 'Reserved for local use',
    'qbm': 'Reserved for local use',
    'qbn': 'Reserved for local use',
    'qbo': 'Reserved for local use',
    'qbp': 'Reserved for local use',
    'qbq': 'Reserved for local use',
    'qbr': 'Reserved for local use',
    'qbs': 'Reserved for local use',
    'qbt': 'Reserved for local use',
    'qbu': 'Reserved for local use',
    'qbv': 'Reserved for local use',
    'qbw': 'Reserved for local use',
    'qbx': 'Reserved for local use',
    'qby': 'Reserved for local use',
    'qbz': 'Reserved for local use',
    'qca': 'Reserved for local use',
    'qcb': 'Reserved for local use',
    'qcc': 'Reserved for local use',
    'qcd': 'Reserved for local use',
    'qce': 'Reserved for local use',
    'qcf': 'Reserved for local use',
    'qcg': 'Reserved for local use',
    'qch': 'Reserved for local use',
    'qci': 'Reserved for local use',
    'qcj': 'Reserved for local use',
    'qck': 'Reserved for local use',
    'qcl': 'Reserved for local use',
    'qcm': 'Reserved for local use',
    'qcn': 'Reserved for local use',
    'qco': 'Reserved for local use',
    'qcp': 'Reserved for local use',
    'qcq': 'Reserved for local use',
    'qcr': 'Reserved for local use',
    'qcs': 'Reserved for local use',
    'qct': 'Reserved for local use',
    'qcu': 'Reserved for local use',
    'qcv': 'Reserved for local use',
    'qcw': 'Reserved for local use',
    'qcx': 'Reserved for local use',
    'qcy': 'Reserved for local use',
    'qcz': 'Reserved for local use',
    'qda': 'Reserved for local use',
    'qdb': 'Reserved for local use',
    'qdc': 'Reserved for local use',
    'qdd': 'Reserved for local use',
    'qde': 'Reserved for local use',
    'qdf': 'Reserved for local use',
    'qdg': 'Reserved for local use',
    'qdh': 'Reserved for local use',
    'qdi': 'Reserved for local use',
    'qdj': 'Reserved for local use',
    'qdk': 'Reserved for local use',
    'qdl': 'Reserved for local use',
    'qdm': 'Reserved for local use',
    'qdn': 'Reserved for local use',
    'qdo': 'Reserved for local use',
    'qdp': 'Reserved for local use',
    'qdq': 'Reserved for local use',
    'qdr': 'Reserved for local use',
    'qds': 'Reserved for local use',
    'qdt': 'Reserved for local use',
    'qdu': 'Reserved for local use',
    'qdv': 'Reserved for local use',
    'qdw': 'Reserved for local use',
    'qdx': 'Reserved for local use',
    'qdy': 'Reserved for local use',
    'qdz': 'Reserved for local use',
    'qea': 'Reserved for local use',
    'qeb': 'Reserved for local use',
    'qec': 'Reserved for local use',
    'qed': 'Reserved for local use',
    'qee': 'Reserved for local use',
    'qef': 'Reserved for local use',
    'qeg': 'Reserved for local use',
    'qeh': 'Reserved for local use',
    'qei': 'Reserved for local use',
    'qej': 'Reserved for local use',
    'qek': 'Reserved for local use',
    'qel': 'Reserved for local use',
    'qem': 'Reserved for local use',
    'qen': 'Reserved for local use',
    'qeo': 'Reserved for local use',
    'qep': 'Reserved for local use',
    'qeq': 'Reserved for local use',
    'qer': 'Reserved for local use',
    'qes': 'Reserved for local use',
    'qet': 'Reserved for local use',
    'qeu': 'Reserved for local use',
    'qev': 'Reserved for local use',
    'qew': 'Reserved for local use',
    'qex': 'Reserved for local use',
    'qey': 'Reserved for local use',
    'qez': 'Reserved for local use',
    'qfa': 'Reserved for local use',
    'qfb': 'Reserved for local use',
    'qfc': 'Reserved for local use',
    'qfd': 'Reserved for local use',
    'qfe': 'Reserved for local use',
    'qff': 'Reserved for local use',
    'qfg': 'Reserved for local use',
    'qfh': 'Reserved for local use',
    'qfi': 'Reserved for local use',
    'qfj': 'Reserved for local use',
    'qfk': 'Reserved for local use',
    'qfl': 'Reserved for local use',
    'qfm': 'Reserved for local use',
    'qfn': 'Reserved for local use',
    'qfo': 'Reserved for local use',
    'qfp': 'Reserved for local use',
    'qfq': 'Reserved for local use',
    'qfr': 'Reserved for local use',
    'qfs': 'Reserved for local use',
    'qft': 'Reserved for local use',
    'qfu': 'Reserved for local use',
    'qfv': 'Reserved for local use',
    'qfw': 'Reserved for local use',
    'qfx': 'Reserved for local use',
    'qfy': 'Reserved for local use',
    'qfz': 'Reserved for local use',
    'qga': 'Reserved for local use',
    'qgb': 'Reserved for local use',
    'qgc': 'Reserved for local use',
    'qgd': 'Reserved for local use',
    'qge': 'Reserved for local use',
    'qgf': 'Reserved for local use',
    'qgg': 'Reserved for local use',
    'qgh': 'Reserved for local use',
    'qgi': 'Reserved for local use',
    'qgj': 'Reserved for local use',
    'qgk': 'Reserved for local use',
    'qgl': 'Reserved for local use',
    'qgm': 'Reserved for local use',
    'qgn': 'Reserved for local use',
    'qgo': 'Reserved for local use',
    'qgp': 'Reserved for local use',
    'qgq': 'Reserved for local use',
    'qgr': 'Reserved for local use',
    'qgs': 'Reserved for local use',
    'qgt': 'Reserved for local use',
    'qgu': 'Reserved for local use',
    'qgv': 'Reserved for local use',
    'qgw': 'Reserved for local use',
    'qgx': 'Reserved for local use',
    'qgy': 'Reserved for local use',
    'qgz': 'Reserved for local use',
    'qha': 'Reserved for local use',
    'qhb': 'Reserved for local use',
    'qhc': 'Reserved for local use',
    'qhd': 'Reserved for local use',
    'qhe': 'Reserved for local use',
    'qhf': 'Reserved for local use',
    'qhg': 'Reserved for local use',
    'qhh': 'Reserved for local use',
    'qhi': 'Reserved for local use',
    'qhj': 'Reserved for local use',
    'qhk': 'Reserved for local use',
    'qhl': 'Reserved for local use',
    'qhm': 'Reserved for local use',
    'qhn': 'Reserved for local use',
    'qho': 'Reserved for local use',
    'qhp': 'Reserved for local use',
    'qhq': 'Reserved for local use',
    'qhr': 'Reserved for local use',
    'qhs': 'Reserved for local use',
    'qht': 'Reserved for local use',
    'qhu': 'Reserved for local use',
    'qhv': 'Reserved for local use',
    'qhw': 'Reserved for local use',
    'qhx': 'Reserved for local use',
    'qhy': 'Reserved for local use',
    'qhz': 'Reserved for local use',
    'qia': 'Reserved for local use',
    'qib': 'Reserved for local use',
    'qic': 'Reserved for local use',
    'qid': 'Reserved for local use',
    'qie': 'Reserved for local use',
    'qif': 'Reserved for local use',
    'qig': 'Reserved for local use',
    'qih': 'Reserved for local use',
    'qii': 'Reserved for local use',
    'qij': 'Reserved for local use',
    'qik': 'Reserved for local use',
    'qil': 'Reserved for local use',
    'qim': 'Reserved for local use',
    'qin': 'Reserved for local use',
    'qio': 'Reserved for local use',
    'qip': 'Reserved for local use',
    'qiq': 'Reserved for local use',
    'qir': 'Reserved for local use',
    'qis': 'Reserved for local use',
    'qit': 'Reserved for local use',
    'qiu': 'Reserved for local use',
    'qiv': 'Reserved for local use',
    'qiw': 'Reserved for local use',
    'qix': 'Reserved for local use',
    'qiy': 'Reserved for local use',
    'qiz': 'Reserved for local use',
    'qja': 'Reserved for local use',
    'qjb': 'Reserved for local use',
    'qjc': 'Reserved for local use',
    'qjd': 'Reserved for local use',
    'qje': 'Reserved for local use',
    'qjf': 'Reserved for local use',
    'qjg': 'Reserved for local use',
    'qjh': 'Reserved for local use',
    'qji': 'Reserved for local use',
    'qjj': 'Reserved for local use',
    'qjk': 'Reserved for local use',
    'qjl': 'Reserved for local use',
    'qjm': 'Reserved for local use',
    'qjn': 'Reserved for local use',
    'qjo': 'Reserved for local use',
    'qjp': 'Reserved for local use',
    'qjq': 'Reserved for local use',
    'qjr': 'Reserved for local use',
    'qjs': 'Reserved for local use',
    'qjt': 'Reserved for local use',
    'qju': 'Reserved for local use',
    'qjv': 'Reserved for local use',
    'qjw': 'Reserved for local use',
    'qjx': 'Reserved for local use',
    'qjy': 'Reserved for local use',
    'qjz': 'Reserved for local use',
    'qka': 'Reserved for local use',
    'qkb': 'Reserved for local use',
    'qkc': 'Reserved for local use',
    'qkd': 'Reserved for local use',
    'qke': 'Reserved for local use',
    'qkf': 'Reserved for local use',
    'qkg': 'Reserved for local use',
    'qkh': 'Reserved for local use',
    'qki': 'Reserved for local use',
    'qkj': 'Reserved for local use',
    'qkk': 'Reserved for local use',
    'qkl': 'Reserved for local use',
    'qkm': 'Reserved for local use',
    'qkn': 'Reserved for local use',
    'qko': 'Reserved for local use',
    'qkp': 'Reserved for local use',
    'qkq': 'Reserved for local use',
    'qkr': 'Reserved for local use',
    'qks': 'Reserved for local use',
    'qkt': 'Reserved for local use',
    'qku': 'Reserved for local use',
    'qkv': 'Reserved for local use',
    'qkw': 'Reserved for local use',
    'qkx': 'Reserved for local use',
    'qky': 'Reserved for local use',
    'qkz': 'Reserved for local use',
    'qla': 'Reserved for local use',
    'qlb': 'Reserved for local use',
    'qlc': 'Reserved for local use',
    'qld': 'Reserved for local use',
    'qle': 'Reserved for local use',
    'qlf': 'Reserved for local use',
    'qlg': 'Reserved for local use',
    'qlh': 'Reserved for local use',
    'qli': 'Reserved for local use',
    'qlj': 'Reserved for local use',
    'qlk': 'Reserved for local use',
    'qll': 'Reserved for local use',
    'qlm': 'Reserved for local use',
    'qln': 'Reserved for local use',
    'qlo': 'Reserved for local use',
    'qlp': 'Reserved for local use',
    'qlq': 'Reserved for local use',
    'qlr': 'Reserved for local use',
    'qls': 'Reserved for local use',
    'qlt': 'Reserved for local use',
    'qlu': 'Reserved for local use',
    'qlv': 'Reserved for local use',
    'qlw': 'Reserved for local use',
    'qlx': 'Reserved for local use',
    'qly': 'Reserved for local use',
    'qlz': 'Reserved for local use',
    'qma': 'Reserved for local use',
    'qmb': 'Reserved for local use',
    'qmc': 'Reserved for local use',
    'qmd': 'Reserved for local use',
    'qme': 'Reserved for local use',
    'qmf': 'Reserved for local use',
    'qmg': 'Reserved for local use',
    'qmh': 'Reserved for local use',
    'qmi': 'Reserved for local use',
    'qmj': 'Reserved for local use',
    'qmk': 'Reserved for local use',
    'qml': 'Reserved for local use',
    'qmm': 'Reserved for local use',
    'qmn': 'Reserved for local use',
    'qmo': 'Reserved for local use',
    'qmp': 'Reserved for local use',
    'qmq': 'Reserved for local use',
    'qmr': 'Reserved for local use',
    'qms': 'Reserved for local use',
    'qmt': 'Reserved for local use',
    'qmu': 'Reserved for local use',
    'qmv': 'Reserved for local use',
    'qmw': 'Reserved for local use',
    'qmx': 'Reserved for local use',
    'qmy': 'Reserved for local use',
    'qmz': 'Reserved for local use',
    'qna': 'Reserved for local use',
    'qnb': 'Reserved for local use',
    'qnc': 'Reserved for local use',
    'qnd': 'Reserved for local use',
    'qne': 'Reserved for local use',
    'qnf': 'Reserved for local use',
    'qng': 'Reserved for local use',
    'qnh': 'Reserved for local use',
    'qni': 'Reserved for local use',
    'qnj': 'Reserved for local use',
    'qnk': 'Reserved for local use',
    'qnl': 'Reserved for local use',
    'qnm': 'Reserved for local use',
    'qnn': 'Reserved for local use',
    'qno': 'Reserved for local use',
    'qnp': 'Reserved for local use',
    'qnq': 'Reserved for local use',
    'qnr': 'Reserved for local use',
    'qns': 'Reserved for local use',
    'qnt': 'Reserved for local use',
    'qnu': 'Reserved for local use',
    'qnv': 'Reserved for local use',
    'qnw': 'Reserved for local use',
    'qnx': 'Reserved for local use',
    'qny': 'Reserved for local use',
    'qnz': 'Reserved for local use',
    'qoa': 'Reserved for local use',
    'qob': 'Reserved for local use',
    'qoc': 'Reserved for local use',
    'qod': 'Reserved for local use',
    'qoe': 'Reserved for local use',
    'qof': 'Reserved for local use',
    'qog': 'Reserved for local use',
    'qoh': 'Reserved for local use',
    'qoi': 'Reserved for local use',
    'qoj': 'Reserved for local use',
    'qok': 'Reserved for local use',
    'qol': 'Reserved for local use',
    'qom': 'Reserved for local use',
    'qon': 'Reserved for local use',
    'qoo': 'Reserved for local use',
    'qop': 'Reserved for local use',
    'qoq': 'Reserved for local use',
    'qor': 'Reserved for local use',
    'qos': 'Reserved for local use',
    'qot': 'Reserved for local use',
    'qou': 'Reserved for local use',
    'qov': 'Reserved for local use',
    'qow': 'Reserved for local use',
    'qox': 'Reserved for local use',
    'qoy': 'Reserved for local use',
    'qoz': 'Reserved for local use',
    'qpa': 'Reserved for local use',
    'qpb': 'Reserved for local use',
    'qpc': 'Reserved for local use',
    'qpd': 'Reserved for local use',
    'qpe': 'Reserved for local use',
    'qpf': 'Reserved for local use',
    'qpg': 'Reserved for local use',
    'qph': 'Reserved for local use',
    'qpi': 'Reserved for local use',
    'qpj': 'Reserved for local use',
    'qpk': 'Reserved for local use',
    'qpl': 'Reserved for local use',
    'qpm': 'Reserved for local use',
    'qpn': 'Reserved for local use',
    'qpo': 'Reserved for local use',
    'qpp': 'Reserved for local use',
    'qpq': 'Reserved for local use',
    'qpr': 'Reserved for local use',
    'qps': 'Reserved for local use',
    'qpt': 'Reserved for local use',
    'qpu': 'Reserved for local use',
    'qpv': 'Reserved for local use',
    'qpw': 'Reserved for local use',
    'qpx': 'Reserved for local use',
    'qpy': 'Reserved for local use',
    'qpz': 'Reserved for local use',
    'qqa': 'Reserved for local use',
    'qqb': 'Reserved for local use',
    'qqc': 'Reserved for local use',
    'qqd': 'Reserved for local use',
    'qqe': 'Reserved for local use',
    'qqf': 'Reserved for local use',
    'qqg': 'Reserved for local use',
    'qqh': 'Reserved for local use',
    'qqi': 'Reserved for local use',
    'qqj': 'Reserved for local use',
    'qqk': 'Reserved for local use',
    'qql': 'Reserved for local use',
    'qqm': 'Reserved for local use',
    'qqn': 'Reserved for local use',
    'qqo': 'Reserved for local use',
    'qqp': 'Reserved for local use',
    'qqq': 'Reserved for local use',
    'qqr': 'Reserved for local use',
    'qqs': 'Reserved for local use',
    'qqt': 'Reserved for local use',
    'qqu': 'Reserved for local use',
    'qqv': 'Reserved for local use',
    'qqw': 'Reserved for local use',
    'qqx': 'Reserved for local use',
    'qqy': 'Reserved for local use',
    'qqz': 'Reserved for local use',
    'qra': 'Reserved for local use',
    'qrb': 'Reserved for local use',
    'qrc': 'Reserved for local use',
    'qrd': 'Reserved for local use',
    'qre': 'Reserved for local use',
    'qrf': 'Reserved for local use',
    'qrg': 'Reserved for local use',
    'qrh': 'Reserved for local use',
    'qri': 'Reserved for local use',
    'qrj': 'Reserved for local use',
    'qrk': 'Reserved for local use',
    'qrl': 'Reserved for local use',
    'qrm': 'Reserved for local use',
    'qrn': 'Reserved for local use',
    'qro': 'Reserved for local use',
    'qrp': 'Reserved for local use',
    'qrq': 'Reserved for local use',
    'qrr': 'Reserved for local use',
    'qrs': 'Reserved for local use',
    'qrt': 'Reserved for local use',
    'qru': 'Reserved for local use',
    'qrv': 'Reserved for local use',
    'qrw': 'Reserved for local use',
    'qrx': 'Reserved for local use',
    'qry': 'Reserved for local use',
    'qrz': 'Reserved for local use',
    'qsa': 'Reserved for local use',
    'qsb': 'Reserved for local use',
    'qsc': 'Reserved for local use',
    'qsd': 'Reserved for local use',
    'qse': 'Reserved for local use',
    'qsf': 'Reserved for local use',
    'qsg': 'Reserved for local use',
    'qsh': 'Reserved for local use',
    'qsi': 'Reserved for local use',
    'qsj': 'Reserved for local use',
    'qsk': 'Reserved for local use',
    'qsl': 'Reserved for local use',
    'qsm': 'Reserved for local use',
    'qsn': 'Reserved for local use',
    'qso': 'Reserved for local use',
    'qsp': 'Reserved for local use',
    'qsq': 'Reserved for local use',
    'qsr': 'Reserved for local use',
    'qss': 'Reserved for local use',
    'qst': 'Reserved for local use',
    'qsu': 'Reserved for local use',
    'qsv': 'Reserved for local use',
    'qsw': 'Reserved for local use',
    'qsx': 'Reserved for local use',
    'qsy': 'Reserved for local use',
    'qsz': 'Reserved for local use',
    'qta': 'Reserved for local use',
    'qtb': 'Reserved for local use',
    'qtc': 'Reserved for local use',
    'qtd': 'Reserved for local use',
    'qte': 'Reserved for local use',
    'qtf': 'Reserved for local use',
    'qtg': 'Reserved for local use',
    'qth': 'Reserved for local use',
    'qti': 'Reserved for local use',
    'qtj': 'Reserved for local use',
    'qtk': 'Reserved for local use',
    'qtl': 'Reserved for local use',
    'qtm': 'Reserved for local use',
    'qtn': 'Reserved for local use',
    'qto': 'Reserved for local use',
    'qtp': 'Reserved for local use',
    'qtq': 'Reserved for local use',
    'qtr': 'Reserved for local use',
    'qts': 'Reserved for local use',
    'qtt': 'Reserved for local use',
    'qtu': 'Reserved for local use',
    'qtv': 'Reserved for local use',
    'qtw': 'Reserved for local use',
    'qtx': 'Reserved for local use',
    'qty': 'Reserved for local use',
    'qtz': 'Reserved for local use',
    'que': 'Quechua',
    'raj': 'Rajasthani',
    'rap': 'Rapanui',
    'rar': 'Rarotongan; Cook Islands Maori',
    'roa': 'Romance languages',
    'roh': 'Romansh',
    'rom': 'Romany',
    'rum': 'Romanian; Moldavian; Moldovan',
    'ron': 'Romanian; Moldavian; Moldovan',
    'run': 'Rundi',
    'rup': 'Aromanian; Arumanian; Macedo-Romanian',
    'rus': 'Russian',
    'sad': 'Sandawe',
    'sag': 'Sango',
    'sah': 'Yakut',
    'sai': 'South American Indian languages',
    'sal': 'Salishan languages',
    'sam': 'Samaritan Aramaic',
    'san': 'Sanskrit',
    'sas': 'Sasak',
    'sat': 'Santali',
    'scn': 'Sicilian',
    'sco': 'Scots',
    'sel': 'Selkup',
    'sem': 'Semitic languages',
    'sga': 'Irish, Old (to 900)',
    'sgn': 'Sign Languages',
    'shn': 'Shan',
    'sid': 'Sidamo',
    'sin': 'Sinhala; Sinhalese',
    'sio': 'Siouan languages',
    'sit': 'Sino-Tibetan languages',
    'sla': 'Slavic languages',
    'slo': 'Slovak',
    'slk': 'Slovak',
    'slv': 'Slovenian',
    'sma': 'Southern Sami',
    'sme': 'Northern Sami',
    'smi': 'Sami languages',
    'smj': 'Lule Sami',
    'smn': 'Inari Sami',
    'smo': 'Samoan',
    'sms': 'Skolt Sami',
    'sna': 'Shona',
    'snd': 'Sindhi',
    'snk': 'Soninke',
    'sog': 'Sogdian',
    'som': 'Somali',
    'son': 'Songhai languages',
    'sot': 'Sotho, Southern',
    'spa': 'Spanish; Castilian',
    'sqi': 'Albanian',
    'srd': 'Sardinian',
    'srn': 'Sranan Tongo',
    'srp': 'Serbian',
    'srr': 'Serer',
    'ssa': 'Nilo-Saharan languages',
    'ssw': 'Swati',
    'suk': 'Sukuma',
    'sun': 'Sundanese',
    'sus': 'Susu',
    'sux': 'Sumerian',
    'swa': 'Swahili',
    'swe': 'Swedish',
    'syc': 'Classical Syriac',
    'syr': 'Syriac',
    'tah': 'Tahitian',
    'tai': 'Tai languages',
    'tam': 'Tamil',
    'tat': 'Tatar',
    'tel': 'Telugu',
    'tem': 'Timne',
    'ter': 'Tereno',
    'tet': 'Tetum',
    'tgk': 'Tajik',
    'tgl': 'Tagalog',
    'tha': 'Thai',
    'tib': 'Tibetan',
    'tig': 'Tigre',
    'tir': 'Tigrinya',
    'tiv': 'Tiv',
    'tkl': 'Tokelau',
    'tlh': 'Klingon; tlhIngan-Hol',
    'tli': 'Tlingit',
    'tmh': 'Tamashek',
    'tog': 'Tonga (Nyasa)',
    'ton': 'Tonga (Tonga Islands)',
    'tpi': 'Tok Pisin',
    'tsi': 'Tsimshian',
    'tsn': 'Tswana',
    'tso': 'Tsonga',
    'tuk': 'Turkmen',
    'tum': 'Tumbuka',
    'tup': 'Tupi languages',
    'tur': 'Turkish',
    'tut': 'Altaic languages',
    'tvl': 'Tuvalu',
    'twi': 'Twi',
    'tyv': 'Tuvinian',
    'udm': 'Udmurt',
    'uga': 'Ugaritic',
    'uig': 'Uighur; Uyghur',
    'ukr': 'Ukrainian',
    'umb': 'Umbundu',
    'und': 'Undetermined',
    'urd': 'Urdu',
    'uzb': 'Uzbek',
    'vai': 'Vai',
    'ven': 'Venda',
    'vie': 'Vietnamese',
    'vol': 'Volapük',
    'vot': 'Votic',
    'wak': 'Wakashan languages',
    'wal': 'Wolaitta; Wolaytta',
    'war': 'Waray',
    'was': 'Washo',
    'wel': 'Welsh',
    'wen': 'Sorbian languages',
    'wln': 'Walloon',
    'wol': 'Wolof',
    'xal': 'Kalmyk; Oirat',
    'xho': 'Xhosa',
    'yao': 'Yao',
    'yap': 'Yapese',
    'yid': 'Yiddish',
    'yor': 'Yoruba',
    'ypk': 'Yupik languages',
    'zap': 'Zapotec',
    'zbl': 'Blissymbols; Blissymbolics; Bliss',
    'zen': 'Zenaga',
    'zgh': 'Standard Moroccan Tamazight',
    'zha': 'Zhuang; Chuang',
    'zho': 'Chinese',
    'znd': 'Zande languages',
    'zul': 'Zulu',
    'zun': 'Zuni',
    'zxx': 'No linguistic content; Not applicable',
    'zza': 'Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki',
}


class MIME_TYPES(object):
    APPLICATION_ACAD = 'application/acad'
    APPLICATION_APPLEFILE = 'application/applefile'
    APPLICATION_ASTOUND = 'application/astound'
    APPLICATION_DSPTYPE = 'application/dsptype'
    APPLICATION_DXF = 'application/dxf'
    APPLICATION_FUTURESPLASH = 'application/futuresplash'
    APPLICATION_GZIP = 'application/gzip'
    APPLICATION_JAVASCRIPT = 'application/javascript'
    APPLICATION_JSON = 'application/json'
    APPLICATION_LISTENUP = 'application/listenup'
    APPLICATION_MAC_BINHEX_40 = 'application/mac-binhex40'
    APPLICATION_MBEDLET = 'application/mbedlet'
    APPLICATION_MIF = 'application/mif'
    APPLICATION_MSEXCEL = 'application/msexcel'
    APPLICATION_MSHELP = 'application/mshelp'
    APPLICATION_MSPOWETPOINT = 'application/mspowerpoint'
    APPLICATION_MSWORD = 'application/msword'
    APPLICATION_OCTET_STREAM = 'application/octet-stream'
    APPLICATION_ODA = 'application/oda'
    APPLICATION_PDF = 'application/pdf'
    APPLICATION_POSTSCRIPT = 'application/postscript'
    APPLICATION_RTC = 'application/rtc'
    APPLICATION_RTF = 'application/rtf'
    APPLICATION_STUDIOM = 'application/studiom'
    APPLICATION_TOOLBOOK = 'application/toolbook'
    APPLICATION_VOCALTEC_MEDIA_DESC = 'application/vocaltec-media-desc'
    APPLICATION_VOCALTEC_MEDIA_FILE = 'application/vocaltec-media-file'
    APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEET = \
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = \
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    APPLICATION_XHTML_XML = 'application/xhtml+xml'
    APPLICATION_XML = 'application/xml'
    APPLICATION_X_BCPIO = 'application/x-bcpio'
    APPLICATION_X_COMPRESS = 'application/x-compress'
    APPLICATION_X_CPIO = 'application/x-cpio'
    APPLICATION_X_CSH = 'application/x-csh'
    APPLICATION_X_DIRECTOR = 'application/x-director'
    APPLICATION_X_DVI = 'application/x-dvi'
    APPLICATION_X_ENVOY = 'application/x-envoy'
    APPLICATION_X_GTAR = 'application/x-gtar'
    APPLICATION_X_HDF = 'application/x-hdf'
    APPLICATION_X_HTTPD_PHP = 'application/x-httpd-php'
    APPLICATION_X_LATEX = 'application/x-latex'
    APPLICATION_X_MACBINARY = 'application/x-macbinary'
    APPLICATION_X_MIF = 'application/x-mif'
    APPLICATION_X_NETCDF = 'application/x-netcdf'
    APPLICATION_X_NSCHAT = 'application/x-nschat'
    APPLICATION_X_SH = 'application/x-sh'
    APPLICATION_X_SHAR = 'application/x-shar'
    APPLICATION_X_SHOCKWAVE_FLASH = 'application/x-shockwave-flash'
    APPLICATION_X_SPRITE = 'application/x-sprite'
    APPLICATION_X_STUFFIT = 'application/x-stuffit'
    APPLICATION_X_SUPERCARD = 'application/x-supercard'
    APPLICATION_X_SV4CPIO = 'application/x-sv4cpio'
    APPLICATION_X_SV4CRC = 'application/x-sv4crc'
    APPLICATION_X_TAR = 'application/x-tar'
    APPLICATION_X_TCL = 'application/x-tcl'
    APPLICATION_X_TEX = 'application/x-tex'
    APPLICATION_X_TEXINFO = 'application/x-texinfo'
    APPLICATION_X_TROFF = 'application/x-troff'
    APPLICATION_X_TROFF_MAN = 'application/x-troff-man'
    APPLICATION_X_TROFF_ME = 'application/x-troff-me'
    APPLICATION_X_TROFF_MS = 'application/x-troff-ms'
    APPLICATION_X_USTAR = 'application/x-ustar'
    APPLICATION_X_WAIS_SOURCE = 'application/x-wais-source'
    APPLICATION_X_WWW_FORM_URLENCODED = 'application/x-www-form-urlencoded'
    APPLICATION_ZIP = 'application/zip'
    AUDIO_BASIC = 'audio/basic'
    AUDIO_ECHOSPEECH = 'audio/echospeech'
    AUDIO_TSPLAYER = 'audio/tsplayer'
    AUDIO_VOXWARE = 'audio/voxware'
    AUDIO_X_AIFF = 'audio/x-aiff'
    AUDIO_X_DSPEEH = 'audio/x-dspeeh'
    AUDIO_X_MIDI = 'audio/x-midi'
    AUDIO_X_MPEG = 'audio/x-mpeg'
    AUDIO_X_PN_REALAUDIO = 'audio/x-pn-realaudio'
    AUDIO_X_PN_REALAUDIO_PLUGIN = 'audio/x-pn-realaudio-plugin'
    AUDIO_X_QT_STREAM = 'audio/x-qt-stream'
    AUDIO_X_WAV = 'audio/x-wav'
    DRAWING_X_DWF = 'drawing/x-dwf'
    IMAGE_BMP = 'image/bmp'
    IMAGE_CIS_COD = 'image/cis-cod'
    IMAGE_CMU_RASTER = 'image/cmu-raster'
    IMAGE_FIF = 'image/fif'
    IMAGE_GIF = 'image/gif'
    IMAGE_IEF = 'image/ief'
    IMAGE_JPEG = 'image/jpeg'
    IMAGE_PNG = 'image/png'
    IMAGE_SVG_XML = 'image/svg+xml'
    IMAGE_TIFF = 'image/tiff'
    IMAGE_VASA = 'image/vasa'
    IMAGE_VND_WAP_WBMP = 'image/vnd.wap.wbmp'
    IMAGE_X_FREEHAND = 'image/x-freehand'
    IMAGE_X_ICON = 'image/x-icon'
    IMAGE_X_PORTABLE_ANYMAP = 'image/x-portable-anymap'
    IMAGE_X_PORTABLE_BITMAP = 'image/x-portable-bitmap'
    IMAGE_X_PORTABLE_GRAYMAP = 'image/x-portable-graymap'
    IMAGE_X_PORTABLE_PIXMAP = 'image/x-portable-pixmap'
    IMAGE_X_RGB = 'image/x-rgb'
    IMAGE_X_WINDOWDUMP = 'image/x-windowdump'
    IMAGE_X_XBITMAP = 'image/x-xbitmap'
    IMAGE_X_XPIXMAP = 'image/x-xpixmap'
    MESSAGE_EXPERNAL_BODY = 'message/external-body'
    MESSAGE_HTTP = 'message/http'
    MESSAGE_NEWS = 'message/news'
    MESSAGE_PARTIAL = 'message/partial'
    MESSAGE_RFC822 = 'message/rfc822'
    MODEL_VRML = 'model/vrml'
    MULTIPART_ALTERNATIVE = 'multipart/alternative'
    MULTIPART_BYTERANGES = 'multipart/byteranges'
    MULTIPART_DIGEST = 'multipart/digest'
    MULTIPART_ENCRYPTED = 'multipart/encrypted'
    MULTIPART_FORM_DATA = 'multipart/form-data'
    MULTIPART_MIXED = 'multipart/mixed'
    MULTIPART_PARALLEL = 'multipart/parallel'
    MULTIPART_RELATED = 'multipart/related'
    MULTIPART_REPORT = 'multipart/report'
    MULTIPART_SIGNED = 'multipart/signed'
    MULTIPART_VOICE_MESSAGE = 'multipart/voice-message'
    TEXT_COMMA_SEPARATED_VALUES = 'text/comma-separated-values'
    TEXT_CSS = 'text/css'
    TEXT_HTML = 'text/html'
    TEXT_JAVASCRIPT = 'text/javascript'
    TEXT_PLAIN = 'text/plain'
    TEXT_RICHTEXT = 'text/richtext'
    TEXT_RTF = 'text/rtf'
    TEXT_TAB_SEPARATED_VALUES = 'text/tab-separated-values'
    TEXT_VND_WAP_WML = 'text/vnd.wap.wml'
    APPLICATION_VND_WAP_WMLC = 'application/vnd.wap.wmlc'
    TEXT_VND_WAP_WMLSCRIPT = 'text/vnd.wap.wmlscript'
    APPLICATION_VND_WAP_WMLSCRIPTC = 'application/vnd.wap.wmlscriptc'
    TEXT_XML = 'text/xml'
    TEXT_XML_EXTERNAL_PARSED_ENTIRY = 'text/xml-external-parsed-entity'
    TEXT_X_SETEXT = 'text/x-setext'
    TEXT_X_SGML = 'text/x-sgml'
    TEXT_X_SPEECH = 'text/x-speech'
    VIDEO_MPEG = 'video/mpeg'
    VIDEO_MP4 = 'video/mp4'
    VIDEO_QUICKTIME = 'video/quicktime'
    VIDEO_VND_VIVO = 'video/vnd.vivo'
    VIDEO_WEBM = 'video/webm'
    VIDEO_X_MSVIDEO = 'video/x-msvideo'
    VIDEO_X_SGI_MOVIE = 'video/x-sgi-movie'
    WORKBOOK_FORMULAONE = 'workbook/formulaone'
    X_WORLD_X_3DMF = 'x-world/x-3dmf'
    X_WORLD_X_VRML = 'x-world/x-vrml'


MIME_TYPES_LIST = [MIME_TYPES.__dict__[i] for i in MIME_TYPES.__dict__.keys() if not i.startswith('__')]


class ID3v2_3_PICTURE_TYPES(object):
    OTHER = '\x00'
    FILE_ICON_32x32 = '\x01'
    OTHER_FILE_ICON = '\x02'
    COVER_FRONT = '\x03'
    COVER_BACK = '\x04'
    LEAFLET_PAGE = '\x05'
    MEDIA = '\x06'
    LEAD_ARTIST_LEAD_PERFORMER_SOLOIST = '\x07'
    ARTIST_PERFORMER = '\x08'
    CONDUCTOR = '\x09'
    BAND_ORCHESTRA = '\x0A'
    COMPOSER = '\x0B'
    LYRICIST_TEXT_WRITER = '\x0C'
    RECORDING_LOCATION = '\x0D'
    DURING_RECORDING = '\x0E'
    DURING_PERFORMANCE = '\x0F'
    MOVIE_VIDEO_SCREEN_CAPTURE = '\x10'
    A_BRIGHT_COLOURED_FISH = '\x11'
    ILLUSTRATION = '\x12'
    BAND_ARTIST_LOGOTYPE = '\x13'
    PUBLISHER_STUDIO_LOGOTYPE = '\x14'


ID3v2_3_PICTURE_TYPES_LIST = [ID3v2_3_PICTURE_TYPES.__dict__[i] for i in ID3v2_3_PICTURE_TYPES.__dict__.keys()
                              if not i.startswith('__')]


# exceptions
class PyID3TaggerException(Exception):
    pass


class PyID3TaggerNotImplementedError(PyID3TaggerException):
    pass


class PyID3TaggerInvalidData(PyID3TaggerException):
    pass


class PyID3TaggerIOError(PyID3TaggerException):
    pass


class PyID3TaggerFilePathException(PyID3TaggerException):
    pass
