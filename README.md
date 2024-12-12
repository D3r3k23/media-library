# Media Library

## Scripts
- Blank content_rating to NR
- Unrated Edition to NR content_rating

### Library Analysis
- Check editions
- Check images
- (?) Check health
- Display people, studios, networks

## Repository Guide
```
media-library
├─── collexions
│    └─── config.json
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
│    ├─── overlays
│    │    ├─── audio
│    │    ├─── source
│    │    ├─── tags
│    │    └─── video
│    ├─── playlists
│    ├─── shows
│    └─── watch
│         └─── mediux
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
│    │    ├─── prerolls
│    │    │    └─── prerolls.yaml
│    │    ├─── seasonal
│    │    │    └─── movies.yaml, shows.yaml, templates.yaml
│    │    ├─── series
│    │    │    └─── both.yaml, movies.yaml, shows.yaml, templates.yaml
│    │    ├─── studios
│    │    │    └─── studios.yaml
│    │    ├─── collectionless.yaml
│    │    └─── templates.yaml
│    ├─── labels
│    │    ├─── audio.yaml
│    │    ├─── editions.yaml
│    │    ├─── favorites.yaml
│    │    ├─── source.yaml
│    │    ├─── tags.yaml
│    │    ├─── templates.yaml
│    │    └─── video.yaml
│    ├─── overlays
│    │    ├─── both.yaml
│    │    ├─── movies.yaml
│    │    ├─── shows.yaml
│    │    └─── templates.yaml
│    ├─── playlists
│    │    └─── playlists.yaml
│    ├─── reports
│    └─── config.yaml
├─── kometa-dev
│    └─── *Same as above*
├─── media
│    ├─── extras
│    │    └─── comedy, movies, shows
│    ├─── library
│    │    └─── comedy, movies, shows
│    ├─── recycle
│    │    └─── comedy, movies, shows
│    ├─── temp
│    │    └─── comedy, movies, shows
│    ├─── test
│    │    └─── comedy, movies, shows
│    ├─── torrents
│    │    ├─── comedy, movies, shows
│    │    └─── torrent
│    └─── usenet
│         ├─── complete
│         │    └─── comedy, movies, shows
│         ├─── downloading
│         └─── nzb
├─── metadata
│    ├─── comedy.yaml
│    ├─── movies.yaml
│    └─── shows.yaml
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
└─── title-card-maker
     └─── config.yaml
