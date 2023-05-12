# 0x19-postmortem

<img src="https://res.cloudinary.com/dkezlmzn1/image/upload/v1683880822/i_have_no_idea_what_i_m_doing_meme_fq96gg.jpg"/>

## Incident: Page server error

Date: May 11th, 2023

Time: 6:45pm - 7:15pm

Affected Users: All users

Impact: Users were unable to access page contents after reloading.

Root Cause: The fetch function in the frontend did not activate on reload.

Resolution: Caching was implemented to display data when reloaded.

Corrective Measures: Thorough testing was performed to ensure that the resolution methods worked.

Preventative Measures: The fetch function will be thoroughly tested before deployment in the future.

## Timeline:

    6:45pm: Beta user reports error when trying to reload page.
    6:50pm: John Diginee is alerted to the error.
    6:55pm: John Diginee determines that the error is caused by the fetch function in the frontend.
    7:00pm: Caching is implemented to display data when reloaded.
    7:15pm: The error is resolved.

## Lessons Learned:

    It is important to thoroughly test all code before deployment.
    It is important to have a process in place for quickly identifying and resolving errors.
    It is important to have a team of people who are able to troubleshoot and resolve errors.

## Recommendations:

    The fetch function will be thoroughly tested before deployment in the future.
    A process will be put in place for quickly identifying and resolving errors.
    A team of people will be trained on how to troubleshoot and resolve errors.

