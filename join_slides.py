filenames = ['1_intro.md', '2_nuclear_data.md', '3_prompt_response.md', '4_delayed_response.md', '5_simulation_software.md']
with open('all_slides.md', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            if fname == filenames[0]:
                for line in infile:
                    outfile.write(line)
            else:
                # find end of the formatting
                end_of_stlye_found = False
                for i, line in enumerate(infile):
                    if end_of_stlye_found:
                        outfile.write(line)
                    if line.startswith('</style>'):
                        end_of_stlye_found = True