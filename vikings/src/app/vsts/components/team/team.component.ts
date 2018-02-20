import { Component, OnInit } from '@angular/core';

import { TestService } from '../../services/test.service';
import { Teammate } from '../../model/teammate';

@Component({
  selector: 'app-team',
  templateUrl: './team.component.html',
  styleUrls: ['./team.component.css']
})
export class TeamComponent implements OnInit {
  teamMates: Teammate[];
  displayedColumns = ['id', 'firstname', 'lastname', 'email'];
  newMate: Teammate;

  constructor(
    private testService: TestService
  ) { }

  ngOnInit() {
    this.testService.getTeam().subscribe(
      res => this.teamMates = res
    );
    this.newMate = {
      id: null,
      firstname: '',
      lastname: '',
      email: ''
    };
  }

  addMember():void {
    this.testService.addMember(this.newMate).subscribe(
      res => this.teamMates.push(this.newMate) 
    )
  }

}
