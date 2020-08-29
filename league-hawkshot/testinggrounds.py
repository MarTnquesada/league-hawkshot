from cassiopeia import cassiopeia as cass


def main():
    cass.set_riot_api_key("RGAPI-e3bb6a6c-94b4-4d81-a346-bbc5571e937a")  # This overrides the value set in your configuration/settings.
    cass.set_default_region("EUW")
    summoner_name = "Larry Calefa"

    summoner = cass.get_summoner(name=summoner_name)
    print("{name} is a level {level} summoner on the {region} server, and his id is {id}.".format(
        name=summoner.name, level=summoner.level, region=summoner.region, id=summoner.id))
    summoner_last_match = cass.get_match_history(summoner=summoner, begin_index=0, end_index=1)[0]
    print(f'The id of this summoner last played game is {summoner_last_match.id}')
    print(f'Listing participants of the match')
    for participant in summoner_last_match.participants:
        print(f'{participant.summoner.name}')
    print(f'Stats for {summoner_name} in this game')
    participant = summoner_last_match.participants[summoner_name]
    print(f'Runes: {participant.runes}\Side: {participant.side}\nRole: {participant.role}\nLane: {participant.lane}')
    print(f'The frames of the timeline of {summoner_name} are {participant.timeline.frames}')
    frame_1 = participant.timeline.frames[0]
    print(frame_1.position.location)


if __name__ == '__main__':
    main()