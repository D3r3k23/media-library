# Media Library

## Scripts
- Blank content_rating to NR
- Unrated Edition to NR content_rating

### Library Analysis
- Check editions
- Check images
- (?) Check health
- Display people, studios, networks

## Media Library
```
media
├─── extras
│    └─── comedy, movies, shows
├─── library
│    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
├─── recycle
│    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
├─── temp-library
│    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
│─── test-library
│    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
├─── torrents
│    ├─── complete
│    │    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
│    ├─── incomplete
│    └─── torrent
└─── usenet
     ├─── complete
     │    └─── audiobooks, comedy, ebooks, fan-edits, movies, movies-4K, music, music-videos, shows, videos
     ├─── incomplete
     └─── nzb
```

## Repository
```
library
├─── collexions
│    └─── config.json
├─── imagemaid
│    └─── .env
├─── images
│    ├─── collections
│    │    ├─── basic
│    │    ├─── charts
│    │    ├─── comedy
│    │    ├─── decades
│    │    ├─── formats
│    │    ├─── genres
│    │    ├─── networks
│    │    ├─── people
│    │    ├─── seasonal
│    │    ├─── series
│    │    └─── studios
│    ├─── comedy
│    ├─── movies
│    ├─── music
│    ├─── overlays
│    │    ├─── audio
│    │    ├─── source
│    │    ├─── tags
│    │    └─── video
│    ├─── playlists
│    ├─── shows
│    └─── title-cards
├─── kometa
│    ├─── collections
│    │    ├─── basic
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── charts
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── comedy
│    │    │    └─── comedians.yaml, comedy.yaml
│    │    ├─── decades
│    │    │    └─── decades.yaml
│    │    ├─── formats
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── genres
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── networks
│    │    │    └─── networks.yaml
│    │    ├─── people
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── seasonal
│    │    │    └─── movies.yaml, shows.yaml, templates.yaml
│    │    ├─── series
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── studios
│    │    │    └─── studios.yaml
│    │    ├─── collectionless.yaml
│    │    ├─── prerolls.yaml
│    │    ├─── refresh.yaml
│    │    └─── templates.yaml
│    ├─── labels
│    │    ├─── audio
│    │    │    └─── audio.yaml, templates.yaml
│    │    ├─── editions
│    │    │    └─── editions.yaml, templates.yaml
│    │    ├─── favorites
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── genres
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── sources
│    │    │    └─── sources.yaml, templates.yaml
│    │    ├─── tags
│    │    │    └─── tags.yaml, templates.yaml
│    │    ├─── video
│    │    │    └─── video.yaml, templates.yaml
│    │    ├─── reset.yaml
│    │    └─── templates.yaml
│    ├─── overlays
│    │    ├─── both.yaml
│    │    ├─── movies.yaml
│    │    ├─── shows.yaml
│    │    └─── templates.yaml
│    ├─── playlists
│    │    └─── playlists.yaml
│    ├─── reports
│    ├─── docker-compose.yml
│    └─── config.yaml
├─── kometa-dev
│    └─── *Same as above*
├─── metadata
│    ├─── comedy.yaml
│    ├─── movies
│    │    └─── movies.yaml, ...
│    └─── shows
│         └─── shows.yaml, ...
├─── plex-trakt-sync
│    └─── config.yaml
├─── posterizarr
│    └─── config.yaml
├─── prerolls
├─── python
│    ├─── analyze.py
│    ├─── download.py
│    ├─── import_extras.py
│    ├─── import_images.py
│    ├─── import_subtitles.py
│    └─── strip_metadata.py
├─── scripts
│    ├─── directorize.py
│    ├─── ls_empty_dirs.py
│    ├─── rm_empty_dirs.py
│    └─── strip_metadata.py
├─── subtitles
│    ├─── comedy
│    ├─── movies
│    └─── shows
├─── titlecardmaker
│    └─── config.yaml
└─── docker-compose.yml
```
