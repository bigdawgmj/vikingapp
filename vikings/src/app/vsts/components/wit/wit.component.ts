import { Component, OnInit } from '@angular/core';

import { TestService } from '../../services/test.service';

@Component({
  selector: 'app-wit',
  templateUrl: './wit.component.html',
  styleUrls: ['./wit.component.css']
})
export class WitComponent implements OnInit {
  sprint: string;
  added: string;

  constructor(
    private testService: TestService
  ) { }

  ngOnInit() {
    this.sprint = '';
  }

  addTraining(): void {
    let sprintObj: Object = {
      sprint: this.sprint
    }
    this.testService.addTraining(sprintObj).subscribe(
      res => this.successAdd(res)
    )

  }

  successAdd(res: Object): void {
    this.added = 'Training Added!'
    setTimeout(() => {
      this.added = '';
    }, 5000);
  }
}
